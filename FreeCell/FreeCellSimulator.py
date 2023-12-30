import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import numpy as np
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Initialize Pygame

pygame.init()

# Constants
CARD_WIDTH, CARD_HEIGHT = 100, 150
WIDTH, HEIGHT = 100+CARD_WIDTH*7*1.2+CARD_WIDTH, 780
FPS = 60
Green = (0, 81, 44)
BLACK = (0, 0, 0)
FONT_SIZE = 48

data_path = 'C:/Users/blake/Documents/VSCode/Python/FreeCell/FreeCellStats.txt'
# data_file = open(data_path, 'w')
# data_file.write("Month\tDay\tYear\tTime\tMoves\tScore\n")
# data_file.close()


# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('FreeCell')

font = pygame.font.Font(None, FONT_SIZE)

def plot_data(path):
    all_data = np.genfromtxt(path, delimiter='\t',skip_header=1)
    dates = np.array(all_data[:,2])
    times = np.array(all_data[:,3])
    moves = np.array(all_data[:,4])
    scores = np.array(all_data[:,5])
    fig = plt.figure(constrained_layout = True)
    ax = fig.add_subplot(2, 2, 1)
    bx = fig.add_subplot(2, 2, 2)
    cx = fig.add_subplot(2, 2, 3)
    dx = fig.add_subplot(2, 2, 4)
    ax.set_xlabel('Scores',fontsize = 15)
    ax.set_ylabel('Number of Occurances',fontsize = 15)
    ax.set_title('Stats')
    ax.hist(scores)

    bx.set_xlabel('Time (min)',fontsize = 15)
    bx.set_ylabel('Number of Occurances',fontsize = 15)
    bx.hist(times,color='red')

    cx.set_xlabel('Scores',fontsize = 15)
    cx.set_ylabel('Times (min)',fontsize = 15)
    cx.scatter(scores,times,c='green')

    dx.set_xlabel('Last '+str(len(scores[-10:]))+' attemps',fontsize = 15)
    dx.set_ylabel('Scores',fontsize = 15)
    dx.scatter(range(1,1+len(scores[-10:])),scores[-10:],c='orange')
    plt.show()

def get_images():
    # Load card images from the "cards" folder
    card_images = []
    cards_folder = 'C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/'  # Folder containing card images
    for filename in os.listdir(cards_folder):
        if filename.endswith("s.png"):
            card_path = os.path.join(cards_folder, filename)
            card_image = pygame.image.load(card_path)
            card_image = pygame.transform.scale(card_image, (CARD_WIDTH, CARD_HEIGHT))# Resize the card image to the desired width and height
            card_images.append(card_image)

    freecell_image = pygame.image.load(cards_folder+'freecell.png')
    freecell_image = pygame.transform.scale(freecell_image, (CARD_WIDTH, CARD_HEIGHT))

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    stack_cards = []
    
    for suit in suits:
        stack_image = pygame.image.load(f'C:/Users/blake/Documents/VSCode/Python/FreeCell/cards/{suit[:-1]}.png')
        stack_image = pygame.transform.scale(stack_image , (CARD_WIDTH, CARD_HEIGHT))
        stack_cards.append(stack_image)
        
    return card_images, freecell_image, stack_cards

def find_movables(game):
    movable = set([])
    zero_count = 0
    cols = []
    firsts = np.zeros(8,dtype=np.int8)
    for j, card in enumerate(game.board):
        if card == 0:
            zero_count +=1
        elif j<66 and game.board[j+1]==0 and zero_count<8:
            col = game.get_col(zero_count)
            cols.append(col)
            firsts[zero_count] = col[-1]
    for i, col in enumerate(cols):
        if game.e_freecells>0 or game.e_rows>0:#all the final cards are able to move if free spot is open
            movable.add(col[-1])
        depth = 1
        works = True
        # movers = col[-1*depth:]
        while works and game.movable >= len(movers := col[-1*depth:]) and depth<= len(col):
            # print(movers)
            old_mover = 0
            depth +=1
            for i, mover in enumerate(movers):
                if i == 0:
                    old_mover = mover
                else:
                    if old_mover&15!= 1+mover&15  or (old_mover<32 and mover<32) or (old_mover>32 and mover>32):
                        works = False
                    old_mover = mover
                if not(works):
                    break
            if works:
                m = movers[0]
                for first in firsts:
                    if not(m in movable) and first != col[-1] and (1+m&15 == first&15  and ((m>32 and first<32) or (m<32 and first>32))):#another row has a viable space
                        movable.add(m)
                    if not(first in movable):
                        suit_num = first >> 4
                        if game.suits[suit_num] == first - suit_num*16 - 1:
                            movable.add(first)
    # print(movable)

def suit_movers(game):
    target_card = np.zeros(4,dtype=np.int8)
    i=0
    for suit_target in game.suits:
        target_card[i] = suit_target + i*16 + 1
        i+=1
    target_card = set(target_card)
    found = []
    for j, card in enumerate(game.board):
        if (j==66 or game.board[j+1] == 0) and card in target_card:
            found.append(card)
    return found



# Function to draw the cards on the screen
def draw_cards(board):
    x, y = 50, 50 #starting coords of the cards
    margin_x, margin_y = CARD_WIDTH*1.2,CARD_HEIGHT*.2 
    for i in range(4):
        window.blit(stack_cards[i], (x, y))
        x += margin_x
    for i in range(4):
        window.blit(freecell_image, (x, y))
        x += margin_x

    y += CARD_HEIGHT*1.2
    x = 50
    y0 = y

    for i in range(8):
        window.blit(freecell_image, (x, y))
        x += margin_x
    x = 50
    order_inds = np.argsort(np.argsort(board[np.logical_not(board==0)])) #this sorts the array, but instead of returning the sorted array, it returns the index of each element in the sorted array
    counter = 0
    zero_count = 0
    for i, card in enumerate(board):
        if zero_count >=8 and card != 0:#top row
            y = 50
            x = 50 + margin_x*(zero_count-8)
            if i == 66 or  game.board[i+1] ==0:
                window.blit(card_images[order_inds[counter]], (x, y))
                if game.selected_card != None and game.selected_card[0]==-1 and zero_count-8 == game.selected_card[1] and zero_count>11:
                    window.blit(overlay, (x, y))
            counter+=1
        elif card == 0:
            y = y0
            x += margin_x
            zero_count +=1
        else:
            window.blit(card_images[order_inds[counter]], (x, y))
            if card == game.selected_card_num:
                    window.blit(overlay, (x, y))
            y += margin_y
            counter+=1

def display_stats(started_game,start_time):
    moves_text = font.render(f"Moves: {MOVES}", True, BLACK)
    score_text = font.render(f"Score: {SCORE}", True, BLACK)
    window.blit(moves_text, (10, 10))
    window.blit(score_text, (175, 10))
    if started_game:
        elapsed_time = round(time.time() - start_time, 0)
        m = int(elapsed_time // 60)
        s = int(elapsed_time - 60*m)
        s = str(s)
        if len(s) == 1:
            s = '0'+s
        timer_text = font.render(f"Time: {m}:{s}", True, BLACK)
        window.blit(timer_text, (WIDTH-200, 10))
        # movable_text = font.render(f"Movable: {game.movable}", True, BLACK)
        # window.blit(movable_text, (WIDTH-400, 10))

def sort_game(game):
    inds = np.zeros(8,dtype=np.int8)
    cols = [[],[],[],[],[],[],[],[]]
    i = 0
    for card in game:
        if card != 0:
            cols[i].append(card)
        else:
            i+=1
        if i == 8:
            break
    for i in range(len(cols)):
        inds[i] = cols[i][0]
    inds.sort()
    # use inds.....
    # j = 0
    # for i in range(8):
    #     for m in range(len(cols[i])):
    #         game[j] = cols[i][m]
    return game

class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.active = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 3)#white
        # pygame.draw.rect(surface, (255, 255, 100), self.rect, 3)#yellow
        text_render = self.font.render(self.text, True, self.text_color)
        surface.blit(text_render, (self.rect.centerx - text_render.get_width() // 2, self.rect.centery - text_render.get_height() // 2))

class Game:
    def __init__(self):
        self.began = False
        self.board = None
        self.selected_card = None
        self.selected_card_num = None
        self.suits = np.zeros(4,dtype=np.int8)
        self.e_rows = 0
        self.e_freecells = 4
        self.movable = 2**self.e_rows*(self.e_freecells+1)
        self.Master_Deck = np.zeros(52,dtype=np.int8)
        i = 0
        for rank in range(1,14):
            for suit in range(4):
                self.Master_Deck[i] = rank + (suit << 4)
                i += 1
    def new_game_board(self):
        self.selected_card = None
        self.selected_card_num = None
        self.suits = np.zeros(4,dtype=np.int8)
        self.e_rows = 0
        self.e_freecells = 4
        self.movable = 2**self.e_rows*(self.e_freecells+1)
        np.random.shuffle(self.Master_Deck)
        self.board = np.zeros(67,dtype=np.int8)
        i=0
        j = 0
        while i +j< 60:
            for m in range(4):
                for n in range(7):
                    self.board[i+j] = self.Master_Deck[i]
                    i += 1
                j += 1
            for m in range(4):
                for n in range(6):
                    self.board[i+j] = self.Master_Deck[i]
                    i += 1
                j += 1
    def get_col(self,ind):
        zero_count = 0
        output = []
        for card in self.board:
            if card == 0:
                zero_count += 1
            elif zero_count == ind:
                output.append(card)
            if zero_count>ind:
                return output
    def select(self, col,row):
        if col == -1:#top row
            if self.selected_card == None:
                if row<4:
                    return None
                if self.get_num(col,row) != None:
                    self.selected_card = (col,row)
                    self.selected_card_num = None
            else:
                if self.selected_card_num != None or row<4:
                    self.move(self.selected_card,(col,row))
                self.selected_card = None
                self.selected_card_num = None
        elif (num:=self.get_num(col,row)) != None:# check if there is a card in the selected place
            if self.selected_card == None:
                self.selected_card = (col,row)
                self.selected_card_num = num
            else:
                self.move(self.selected_card,(col,row))
                self.selected_card = None
                self.selected_card_num = None
        elif row == -1:#empty row
            self.move(self.selected_card,(col,row))
            self.selected_card = None
            self.selected_card_num = None
    def move(self,card1,card2):
        global MOVES, SCORE
        if card1[0]>-1:
            if card2[0]>=0:#bottom row moves
                n1 = self.get_num(card1[0],card1[1])
                n2 = self.get_num(card2[0],card2[1])
                col = self.get_col(card1[0])
                movers = []
                found = False
                for card in col:
                    if card == n1:
                        found = True
                    if found:
                        movers.append(card)
                if len(movers)> self.movable:
                    works = False
                else:
                    old_mover = 0
                    works = True
                    for i, mover in enumerate(movers):
                        if i == 0:
                            old_mover = mover
                        else:
                            if old_mover&15!= 1+mover&15  or (old_mover<32 and mover<32) or (old_mover>32 and mover>32):
                                works = False
                            old_mover = mover
                        if not(works):
                            break
                if n2 == None:#move to open row
                    if works and len(movers) <= min(2**(self.e_rows-1)*(self.e_freecells+1),13):
                        new_board = np.zeros(67,dtype=np.int8)
                        i = 0
                        zero_count = 0
                        for j, card in enumerate(self.board):
                            if not(card in movers):
                                if card == 0:
                                    zero_count += 1
                                    if j != 66 and zero_count-1 == card2[0]:
                                        for move in movers:
                                            new_board[i] = move
                                            i+=1
                                new_board[i] = card
                                i+=1
                        self.board = new_board
                        if not(not(movers)):
                            MOVES +=1
                            SCORE +=1
                            self.e_rows -= 1
                elif n2&15 == 1+n1&15 and ((n1>32 and n2<32) or (n1<32 and n2>32)) and works:
                    new_board = np.zeros(67,dtype=np.int8)
                    i = 0
                    happened = False
                    for j, card in enumerate(self.board):
                        if not(card in movers):
                            new_board[i] = card
                            i+=1
                            if card == n2 and self.board[j+1] == 0:
                                happened = True
                                for move in movers:
                                    new_board[i] = move
                                    i+=1
                    if happened:
                        self.board = new_board
                        if not(not(movers)):
                            MOVES +=1
                            SCORE +=1
                            if len(movers) == len(col):
                                self.e_rows += 1
            elif card2[0]==-1:#top row
                if card2[1]>3:#freecells
                    n1 = self.get_num(card1[0],card1[1])
                    col = self.get_col(card1[0])
                    empty = False
                    if n1 == col[-1]:#check if n1 is legal to move to the freecell
                        empty = True
                        i = 0
                        zero_count = 0
                        new_board = np.zeros(67,dtype=np.int8)
                        for j, card in enumerate(self.board):
                            if card == 0:
                                zero_count +=1
                                if zero_count == 8+card2[1]:
                                    if j !=66 and self.board[j+1]!=0:
                                        empty = False
                                        break
                                    new_board[i+1] = n1
                                    i+=2
                                else:
                                    i+=1    
                            elif card != n1:
                                new_board[i] = card
                                i+=1
                    if empty:
                        self.board = new_board
                        MOVES +=1
                        SCORE +=1
                        self.e_freecells -= 1
                        if len(col) ==1:
                            self.e_rows +=1
                elif card2[1]>=0:#suit stacks
                    n1 = self.get_num(card1[0],card1[1])
                    if (suit_num := n1 >> 4) == card2[1] and game.suits[suit_num] == n1 - suit_num*16 - 1:
                        col = self.get_col(card1[0])
                        if n1 == col[-1]:#check if n1 is legal to move to the suit stack
                            zero_count = 0
                            i = 0
                            new_board = np.zeros(67,dtype=np.int8)
                            for j, card in enumerate(self.board):
                                if card == 0:
                                    zero_count +=1
                                    if zero_count == 9+card2[1]:
                                        new_board[i] = n1
                                        i+=2
                                    else:
                                        i+=1    
                                elif card != n1:
                                    new_board[i] = card
                                    i+=1
                        self.board = new_board
                        MOVES +=1
                        self.suits[suit_num] += 1
                        if len(col) == 1:
                            self.e_rows+=1               
        elif card1[1]>3:#free cell originating moves
            n1 = self.get_num(card1[0],card1[1])
            n2 = self.get_num(card2[0],card2[1])
            col = self.get_col(card2[0])
            if card2[1] == -1:#to empty row
                i = 0
                new_board = np.zeros(67,dtype=np.int8)
                zero_count = 0
                for j, card in enumerate(self.board):
                    if card != n1:
                        if card == 0:
                            zero_count += 1
                            if j != 66 and zero_count-1 == card2[0]:
                                new_board[i] = n1
                                i+=1
                        new_board[i] = card
                        i+=1
                self.board = new_board
                MOVES +=1
                SCORE +=1
                self.e_rows -= 1
                self.e_freecells +=1
            elif card2[0]>=0:
                if n2 == col[-1] and n2&15 == 1+n1&15 and ((n1>32 and n2<32) or (n1<32 and n2>32)):
                    i = 0
                    new_board = np.zeros(67,dtype=np.int8)
                    for j, card in enumerate(self.board):
                        if card == n2:
                            new_board[i] = n2
                            new_board[i+1] = n1
                            i+=2 
                        elif card != n1:
                            new_board[i] = card
                            i+=1
                    self.board = new_board
                    MOVES +=1
                    SCORE +=1
                    self.e_freecells += 1
            elif card2[0] == -1 and card2[1]>=0:
                n1 = self.get_num(card1[0],card1[1])
                if (suit_num := n1 >> 4) == card2[1] and game.suits[suit_num] == n1 - suit_num*16 - 1:
                    zero_count = 0
                    i = 0
                    new_board = np.zeros(67,dtype=np.int8)
                    for j, card in enumerate(self.board):
                        if card == 0:
                            zero_count +=1
                            if zero_count == 9+card2[1]:
                                new_board[i] = n1
                                i+=2
                            else:
                                i+=1    
                        elif card != n1:
                            new_board[i] = card
                            i+=1
                    self.board = new_board
                    MOVES +=1
                    self.suits[suit_num] += 1
                    self.e_freecells+=1
        self.movable = min(2**self.e_rows*(self.e_freecells+1),13)
        if self.suits[0] == 13 and self.suits[1] == 13 and self.suits[2] == 13 and self.suits[3] == 13:
            self.winner()
        find_movables(game)
    def get_num(self,col,row):
        if col>=0:
            zero_count = 0
            row_count = 0
            for card in self.board:
                if card == 0:
                    zero_count += 1
                elif zero_count == col:
                    if row == row_count:
                        return card
                    else:
                        row_count+=1
        elif col == -1:
            zero_count = 0
            for card in self.board:
                if card == 0:
                    zero_count += 1
                elif zero_count -8 == row:
                    return card
    def get_coords(self,num):
        zero_count = 0
        i = 0
        for j,card in enumerate(self.board):
            if card == 0:
                zero_count += 1
                i = 0
            else:
                if card == num:
                    if zero_count <8:
                        return (zero_count,i)
                    elif card == num:
                        return (-1,zero_count-8)
                i+=1
    def winner(self):
        global start_time, MOVES, SCORE, data_path
        final_time = time.time() - start_time
        current_date = datetime.now()
        formatted_date = current_date.strftime("%m\t%d\t%Y")
        self.began = False
        data_file = open(data_path, 'a')
        data_file.write(formatted_date + "\t" +  str(final_time/60) + "\t" + str(MOVES) + "\t" + str(SCORE)+"\n")
        data_file.close()
        plot_data(data_path)



card_images, freecell_image, stack_cards = get_images()

overlay = pygame.Surface((CARD_WIDTH, CARD_HEIGHT), pygame.SRCALPHA)
overlay.fill((128, 128, 128, 128))


# Main game loop
running = True
clock = pygame.time.Clock()
# Variables for moves and score

MOVES = 0
SCORE = 0

# New game Button properties
ng_button_color = (100, 100, 100) #rgb
# ng_button_color = (0, 0, 75) #rgb
ng_button_color = (175, 0, 0)
ng_button_text_color = (255, 255, 255) #rgb
ng_button_text_color = (255, 255, 100)

ng_button_text = "New Game"
ng_button_width = 180
ng_button_height = 42
ng_button_y = 5
ng_button_center_offset = -100

ng_button_rect = pygame.Rect((WIDTH - ng_button_width)// 2+ng_button_center_offset, ng_button_y, ng_button_width, ng_button_height)
start_button = Button((WIDTH - ng_button_width)// 2+ng_button_center_offset, ng_button_y, ng_button_width, ng_button_height, ng_button_color, ng_button_text, ng_button_text_color, font)

# Auto move Button properties
am_button_color = (100, 100, 100) #rgb
# am_button_color = (0, 0, 75) #rgb
am_button_color = (175, 0, 0)
# _button_color = (200, 0, 0)
am_button_text_color = (255, 255, 255) #rgb
am_button_text_color = (255, 255, 100)
am_button_text = "Auto-Move"
am_button_width = 185
am_button_height = 42
am_button_y = 5
am_button_center_offset = 100

am_button_rect = pygame.Rect((WIDTH - am_button_width)// 2+am_button_center_offset, am_button_y, am_button_width, am_button_height)
am_button = Button((WIDTH - am_button_width)// 2+am_button_center_offset, am_button_y, am_button_width, am_button_height, am_button_color, am_button_text, am_button_text_color, font)

#timer intiailization
game = Game()
start_time = time.time()
while running:
    window.fill(Green)
    for event in pygame.event.get(): #handle events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Left mouse button clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if ng_button_rect.collidepoint(mouse_x, mouse_y):
                start_button.active = True
                start_time = time.time()
                # print("New Game started!")
                MOVES = 0
                SCORE = 0
                game.new_game_board()
            elif am_button_rect.collidepoint(mouse_x, mouse_y):
                if game.began:
                    game.selected_card = None
                    game.selected_card_num = None
                    while len(movers :=suit_movers(game))>0:
                        for j, card in enumerate(game.board):
                            if card in movers:
                                x,y = game.get_coords(card)
                                game.select(x,y)
                                game.select(-1, card >> 4)
            elif game.began:
                col_ind = int((start:=(mouse_x-50)) //(CARD_WIDTH*1.2))
                if start-CARD_WIDTH*1.2*col_ind<=CARD_WIDTH and col_ind<8: #this finds the index of the row
                    if mouse_y <CARD_HEIGHT+50 and mouse_y>50:
                        game.select(-1,col_ind)
                    elif mouse_y > (y0 :=(50 + CARD_HEIGHT*1.2)):
                        y_rel = mouse_y-y0
                        max_row = int(y_rel//(CARD_HEIGHT*.2))#this is the index of the last card that could be clicked on
                        min_row = int(max(0,max_row-4))#this is the index of the first card that could be clicked on
                        #try the max first and then interate to the min
                        l = len(game.get_col(col_ind))
                        if (l -1 >= min_row and l-1 <= max_row) or (game.selected_card != None and l ==0):
                            game.select(col_ind,l-1)
                        elif l -1>= min_row:
                            game.select(col_ind,max_row)
                        else:
                            game.selected_card = None
                            game.selected_card_num = None
                    else:
                        game.selected_card = None
                        game.selected_card_num = None
                else:
                    game.selected_card = None
                    game.selected_card_num = None

    start_button.draw(window)
    am_button.draw(window)
    
    display_stats(game.began,start_time)

    # If button is clicked, show cards and play game
    if start_button.active:
        draw_cards(game.board)
        game.began = True
        start_button.active = False
    elif game.began:
        draw_cards(game.board)
    
    
    pygame.display.flip()
    clock.tick(FPS)