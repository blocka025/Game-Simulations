import random
import copy
import math

class game:
    def __init__(self):
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.has_lost = False
    def print(self):
        for r in range(4):
            for c in range(4):
                print("|",end="")
                if len(str(self.grid[r][c])) < 3:
                    print(self.grid[r][c],end="\t\t")
                else:
                    print(self.grid[r][c],end="\t")
            print("|")

        print("Score =",self.score)
    def add(self,count):
        a = 0 
        for n in range(count):
            while a == 0:
                r = random.randint(0,3)
                c = random.randint(0,3)
                if self.grid[r][c] == 0:
                    a = random.randint(1,10)
                    if a > 1:
                        self.grid[r][c] = 2
                    else:
                        self.grid[r][c] = 4
            a = 0
        self.nobitches()
    def begin(self):
        self.add(2)
    def clear(self):
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    def nobitches(self):
        for c in range(4):
            for r in range(4):
                if self.grid[r][c] == 0:
                    return False
        if self.grid == wboard(self.grid) and self.grid == sboard(self.grid) and self.grid == dboard(self.grid) and self.grid == aboard(self.grid):
            self.has_lost = True
            return True
        else:
            return False
            
    def up(self,p = True):
        old = copy.deepcopy(self.grid)
        for c in range(4):
            nonz = []
            for r in range(4):
                if self.grid[r][c] != 0:
                    nonz.append(self.grid[r][c])
            output = []
            if len(nonz) == 4:
                if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0] 
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                elif nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                    output.append(nonz[3])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                    output.append(nonz[3])
                elif nonz[2] == nonz[3]:
                    output.append(nonz[0])
                    output.append(nonz[1])
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                else:
                    output = nonz
            elif len(nonz) == 3:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                else:
                    output = nonz
            elif len(nonz) == 2:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                else:
                    output = nonz
            elif len(nonz) == 1:
                output = nonz

            for r in range(len(output)):
                self.grid[r][c] = output[r]
            while len(output) < 4:
                self.grid[len(output)][c] = 0
                output.append(0)
        if old != self.grid:
            self.add(1)
            if p:
                self.print()

        
    def down(self, p = True):
        old = copy.deepcopy(self.grid)
        for c in range(4):
            nonz = []
            for r in range(3,-1,-1):
                if self.grid[r][c] != 0:
                    nonz.append(self.grid[r][c])
            output = []
            if len(nonz) == 4:
                if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0] 
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                elif nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                    output.append(nonz[3])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                    output.append(nonz[3])
                elif nonz[2] == nonz[3]:
                    output.append(nonz[0])
                    output.append(nonz[1])
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                else:
                    output = nonz
            elif len(nonz) == 3:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                else:
                    output = nonz
            elif len(nonz) == 2:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                else:
                    output = nonz
            elif len(nonz) == 1:
                output = nonz
            for r in range(len(output)):
                self.grid[3-r][c] = output[r]
            while len(output) < 4:
                self.grid[3-len(output)][c] = 0
                output.append(0)
        if old != self.grid:
            self.add(1)
            if p:
                self.print()
    
    def left(self, p = True):
        old = copy.deepcopy(self.grid)
        for r in range(4):
            nonz = []
            for c in range(4):
                if self.grid[r][c] != 0:
                    nonz.append(self.grid[r][c])
            output = []
            if len(nonz) == 4:
                if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0] 
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                elif nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                    output.append(nonz[3])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                    output.append(nonz[3])
                elif nonz[2] == nonz[3]:
                    output.append(nonz[0])
                    output.append(nonz[1])
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                else:
                    output = nonz
            elif len(nonz) == 3:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                else:
                    output = nonz
            elif len(nonz) == 2:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                else:
                    output = nonz
            elif len(nonz) == 1:
                output = nonz
            for c in range(len(output)):
                self.grid[r][c] = output[c]
            while len(output) < 4:
                self.grid[r][len(output)] = 0
                output.append(0)
        if old != self.grid:
            self.add(1)
            if p:
                self.print()

        
    def right(self,p = True):
        old = copy.deepcopy(self.grid)
        for r in range(4):
            nonz = []
            for c in range(3,-1,-1):
                if self.grid[r][c] != 0:
                    nonz.append(self.grid[r][c])
            output = []
            if len(nonz) == 4:
                if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0] 
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                elif nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                    output.append(nonz[3])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                    output.append(nonz[3])
                elif nonz[2] == nonz[3]:
                    output.append(nonz[0])
                    output.append(nonz[1])
                    output.append(2 * nonz[2])
                    self.score += 2 * nonz[2]
                else:
                    output = nonz
            elif len(nonz) == 3:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                    output.append(nonz[2])
                elif nonz[1] == nonz[2]:
                    output.append(nonz[0])
                    output.append(2 * nonz[1])
                    self.score += 2 * nonz[1]
                else:
                    output = nonz
            elif len(nonz) == 2:
                if nonz[0] == nonz[1]:
                    output.append(2 * nonz[0])
                    self.score += 2 * nonz[0]
                else:
                    output = nonz
            elif len(nonz) == 1:
                output = nonz
            for c in range(len(output)):
                self.grid[r][3-c] = output[c]
            while len(output) < 4:
                self.grid[r][3-len(output)] = 0
                output.append(0)
        if old != self.grid:
            self.add(1)
            if p:
                self.print()

    def gettiles(self):
        tiles = {}
        for a in range(4):
            for b in range(4):
                if self.grid[a][b] != 0:
                    if self.grid[a][b] in tiles:
                        tiles[self.grid[a][b]] += 1
                    else:
                        tiles[self.grid[a][b]] = 1
        return tiles
        
def start(p = True):
    board = game()
    board.add(2)
    if p:
        board.print()
    return board

def player(game):
    while not(game.has_lost):
        
        points = {}
        check = False
        p = True
        if check:
            print("w")
        if wboard(game.grid) != game.grid:
            best = []
            for r in range(4):
                for c in range(4):
                    w = wboard(game.grid)
                    if w[r][c] == 0:
                        w[r][c] = 2
                        best.append(scoring(wboard(w)))
                        best.append(scoring(aboard(w)))
                        best.append(scoring(sboard(w)))
                        best.append(scoring(dboard(w)))
                        w[r][c] = 4
                        best.append(scoring(wboard(w)))
                        best.append(scoring(aboard(w)))
                        best.append(scoring(sboard(w)))
                        best.append(scoring(dboard(w)))       
            points["up"] = 2*sum(best)/len(best)
        if check:
            print("a")
        if aboard(game.grid) != game.grid:
            best = []
            for r in range(4):
                for c in range(4):
                    a = aboard(game.grid)
                    if a[r][c] == 0:
                        a[r][c] = 2
                        best.append(scoring(wboard(a)))
                        best.append(scoring(aboard(a)))
                        best.append(scoring(sboard(a)))
                        best.append(scoring(dboard(a)))
                        a[r][c] = 4
                        best.append(scoring(wboard(a)))
                        best.append(scoring(aboard(a)))
                        best.append(scoring(sboard(a)))
                        best.append(scoring(dboard(a)))
            points["left"] = 2*sum(best)/len(best)
        if check:
            print("s")
        if sboard(game.grid) != game.grid:
            best = []
            for r in range(4):
                for c in range(4):
                    s = sboard(game.grid)
                    if s[r][c] == 0:
                        s[r][c] = 2
                        best.append(scoring(wboard(s)))
                        best.append(scoring(aboard(s)))
                        best.append(scoring(sboard(s)))
                        best.append(scoring(dboard(s)))
                        s[r][c] = 4
                        best.append(scoring(wboard(s)))
                        best.append(scoring(aboard(s)))
                        best.append(scoring(sboard(s)))
                        best.append(scoring(dboard(s)))
            points["down"] = 2*sum(best)/len(best)
        if check:
            print("d")
        if dboard(game.grid) != game.grid:
            best = []
            for r in range(4):
                for c in range(4):
                    d = dboard(game.grid)
                    if d[r][c] == 0:
                        d[r][c] = 2
                        best.append(scoring(wboard(d)))
                        best.append(scoring(aboard(d)))
                        best.append(scoring(sboard(d)))
                        best.append(scoring(dboard(d)))
                        d[r][c] = 4
                        best.append(scoring(wboard(d)))
                        best.append(scoring(aboard(d)))
                        best.append(scoring(sboard(d)))
                        best.append(scoring(dboard(d)))
            points["right"] = 2*sum(best)/len(best)
        print(scoring(game.grid))
        for val in sorted(points.values(),reverse = True):
             if p:
                 
                 for key in points.keys():
                    if points[key] == val:
                        print(key,"=\t",points[key])
                        break
        
        a = input(">")
        if a == 'w':
            game.up()
        elif a == 's':
            game.down()
        elif a == 'a':
            game.left()
        elif a == 'd':
            game.right()
    print("No Bitches")
#player(start())

def reallysmartgoatedaisupercomputer():
    top = [0,[]]
    games = []
    p = False
    #p = False
    check = True
    check = False
    for n in range(5):
        game = start(p)
        #ratmode = False
        while not(game.has_lost):
            #start v2!
            points = {}
            '''if not(ratmode):
            rat = check_rat(game.grid)
        if not(ratmode) and not(rat[0]):'''
            if check:
                print("w")
            if wboard(game.grid) != game.grid:
                best = []
                for r in range(4):
                    for c in range(4):
                        w = wboard(game.grid)
                        if w[r][c] == 0:
                            w[r][c] = 2
                            two = []
                            four = []
                            two.append(.9*scoring(wboard(w)))
                            two.append(.9*scoring(aboard(w)))
                            two.append(.9*scoring(sboard(w)))
                            two.append(.9*scoring(dboard(w)))
                            w[r][c] = 4
                            four.append(.1*scoring(wboard(w)))
                            four.append(.1*scoring(aboard(w)))
                            four.append(.1*scoring(sboard(w)))
                            four.append(.1*scoring(dboard(w)))
                            best.append(max(two))
                            best.append(max(four))
                points["up"] = 2*sum(best)/len(best)
            if check:
                print("a")
            if aboard(game.grid) != game.grid:
                best = []
                for r in range(4):
                    for c in range(4):
                        a = aboard(game.grid)
                        if a[r][c] == 0:
                            a[r][c] = 2
                            two = []
                            four = []
                            two.append(.9*scoring(wboard(a)))
                            two.append(.9*scoring(aboard(a)))
                            two.append(.9*scoring(sboard(a)))
                            two.append(.9*scoring(dboard(a)))
                            a[r][c] = 4
                            four.append(.1*scoring(wboard(a)))
                            four.append(.1*scoring(aboard(a)))
                            four.append(.1*scoring(sboard(a)))
                            four.append(.1*scoring(dboard(a)))
                            best.append(max(two))
                            best.append(max(four))
                points["left"] = 2*sum(best)/len(best)
            if check:
                print("s")
            if sboard(game.grid) != game.grid:
                best = []
                for r in range(4):
                    for c in range(4):
                        s = sboard(game.grid)
                        if s[r][c] == 0:
                            s[r][c] = 2
                            two = []
                            four = []
                            two.append(.9*scoring(wboard(s)))
                            two.append(.9*scoring(aboard(s)))
                            two.append(.9*scoring(sboard(s)))
                            two.append(.9*scoring(dboard(s)))
                            s[r][c] = 4
                            four.append(.1*scoring(wboard(s)))
                            four.append(.1*scoring(aboard(s)))
                            four.append(.1*scoring(sboard(s)))
                            four.append(.1*scoring(dboard(s)))
                            best.append(max(two))
                            best.append(max(four))
                points["down"] = 2*sum(best)/len(best)
            if check:
                print("d")
            if dboard(game.grid) != game.grid:
                best = []
                for r in range(4):
                    for c in range(4):
                        d = dboard(game.grid)
                        if d[r][c] == 0:
                            d[r][c] = 2
                            two = []
                            four = []
                            two.append(.9*scoring(wboard(d)))
                            two.append(.9*scoring(aboard(d)))
                            two.append(.9*scoring(sboard(d)))
                            two.append(.9*scoring(dboard(d)))
                            d[r][c] = 4
                            four.append(.1*scoring(wboard(d)))
                            four.append(.1*scoring(aboard(d)))
                            four.append(.1*scoring(sboard(d)))
                            four.append(.1*scoring(dboard(d)))
                            best.append(max(two))
                            best.append(max(four))
                points["right"] = 2*sum(best)/len(best)
            
            #end v2!
                '''else:
                print("there's a rat!",rat[1],rat[2],rat[3])
                if ratmode == False:
                    ratmode = True
                    ratval = rat[1]
                    r = rat[2]
                    c = rat[3]
                if check:
                    print("w")
                if wboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            w = wboard(game.grid)
                            if w[r][c] == 0:
                                w[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*ratscoring(wboard(w),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(aboard(w),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(sboard(w),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(dboard(w),rat[1],rat[2],rat[3]))
                                w[r][c] = 4
                                four.append(.1*ratscoring(wboard(w),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(aboard(w),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(sboard(w),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(dboard(w),rat[1],rat[2],rat[3]))
                                best.append(max(two))
                                best.append(max(four))
                    points["up"] = 2*sum(best)/len(best)
                if check:
                    print("a")
                if aboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            a = aboard(game.grid)
                            if a[r][c] == 0:
                                a[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*ratscoring(wboard(a),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(aboard(a),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(sboard(a),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(dboard(a),rat[1],rat[2],rat[3]))
                                a[r][c] = 4
                                four.append(.1*ratscoring(wboard(a),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(aboard(a),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(sboard(a),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(dboard(a),rat[1],rat[2],rat[3]))
                                best.append(max(two))
                                best.append(max(four))
                    points["left"] = 2*sum(best)/len(best)
                if check:
                    print("s")
                if sboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            s = sboard(game.grid)
                            if s[r][c] == 0:
                                s[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*ratscoring(wboard(s),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(aboard(s),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(sboard(s),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(dboard(s),rat[1],rat[2],rat[3]))
                                s[r][c] = 4
                                four.append(.1*ratscoring(wboard(s),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(aboard(s),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(sboard(s),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(dboard(s),rat[1],rat[2],rat[3]))
                                best.append(max(two))
                                best.append(max(four))
                    points["down"] = 2*sum(best)/len(best)
                if check:
                    print("d")
                if dboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            d = dboard(game.grid)
                            if d[r][c] == 0:
                                d[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*ratscoring(wboard(d),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(aboard(d),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(sboard(d),rat[1],rat[2],rat[3]))
                                two.append(.9*ratscoring(dboard(d),rat[1],rat[2],rat[3]))
                                d[r][c] = 4
                                four.append(.1*ratscoring(wboard(d),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(aboard(d),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(sboard(d),rat[1],rat[2],rat[3]))
                                four.append(.1*ratscoring(dboard(d),rat[1],rat[2],rat[3]))
                                best.append(max(two))
                                best.append(max(four))
                    points["right"] = 2*sum(best)/len(best)

                    
            for val in sorted(points.values(),reverse = True):
                 if ratmode:#if p:
                     for key in points.keys():
                        break
                        if points[key] == val:
                            print(key,"=\t",points[key])
                            break'''
            
            if p:
                input()
                #pass
            m = max(points.values())
            if "up" in points and m == points["up"]:
                game.up(p)     
            elif "left" in points and m == points["left"]:
                game.left(p)
            elif "down" in points and m == points["down"]:
                game.down(p) 
            elif "right" in points and m == points["right"]:
                game.right(p)
            '''if ratmode and game.grid[rat[2]][rat[3]] != rat[1]:
                ratmode = False
                print("dead rat")'''
                
        a = copy.deepcopy(game.grid)
        b = copy.deepcopy(game.score)
        games.append(a)
        if game.score > top[0]:
            top =[b,a]
    print(top)
    print(games)

'''def sum(game):
    tiles = game.tiles()
    sum = 0
    for key in tiles.keys():
        sum += tiles[key]
    return sum'''
def scoring(board):
    #scoring v1
    #print(board)
    check = True
    check = False
    tiles = gettiles(board)
    score = 0
    box= -1
    for r in range(4):
        if r % 2 == 0:
            for c in range(4):
                box +=1
                if check:
                    print("r=",r,'c=',c,score,tiles,box)
                    #print("tile =",sorted(tiles.keys(),reverse = True)[0])
                if board[r][c] == sorted(tiles.keys(),reverse = True)[0]:
                    score += math.exp(-box) * board[r][c]
                                                       #score += math.exp(-box) * math.log(board[r][c],2)
                    #print(math.log(board[r][c],2))
                #elif board[r][c]//sorted(tiles.keys(),reverse = True)[0]>8:
                    #score -= math.exp(-2*box) * board[r][c]//sorted(tiles.keys(),reverse = True)[0] 
                elif board[r][c] != 0:
                    score += math.exp(-2*box) * board[r][c]    
                    #score += math.exp(-2*box) * math.log(board[r][c],2)
                if board[r][c] != 0:
                    #print("titties:")
                    tiles[board[r][c]] -= 1
                    if tiles[board[r][c]] == 0:
                        tiles.pop(board[r][c])
                        if len(tiles) == 0:
                            return score
        elif r % 2 == 1:
            for c in range(3,-1,-1):
                box +=1
                if check:
                    print("r=",r,'c=',c,score,tiles,box)
                if board[r][c] == sorted(tiles.keys(),reverse = True)[0]:
                    score += math.exp(-box) * board[r][c] 
                    #score += math.exp(-box) * math.log(board[r][c],2)
                elif board[r][c] != 0:
                    score += math.exp(-2*box) * board[r][c]
                    #score += math.exp(-2*box) * math.log(board[r][c],2)
                if board[r][c] != 0:
                    tiles[board[r][c]] -= 1
                    if tiles[board[r][c]] == 0:
                        tiles.pop(board[r][c])
                        if len(tiles) == 0:
                            return score
    return score

def gettiles(board):
    tiles = {}
    for a in range(4):
        for b in range(4):
            if board[a][b] != 0:
                if board[a][b] in tiles:
                    tiles[board[a][b]] += 1
                else:
                    tiles[board[a][b]] = 1
    return tiles

def wboard(grid):
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for c in range(4):
        nonz = []
        for r in range(4):
            if grid[r][c] != 0:
                nonz.append(grid[r][c])
        output = []
        score = 0
        if len(nonz) == 4: 
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
                output.append(nonz[3])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
                output.append(nonz[3])
            elif nonz[2] == nonz[3]:
                output.append(nonz[0])
                output.append(nonz[1])
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            elif nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0] 
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            else:
                output = nonz
        elif len(nonz) == 3:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
            else:
                output = nonz
        elif len(nonz) == 2:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
            else:
                output = nonz
        elif len(nonz) == 1:
            output = nonz
        for r in range(len(output)):
            mat[r][c] = output[r]
        while len(output) < 4:
            mat[len(output)][c] = 0
            output.append(0)
    return mat

def sboard(grid):
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for c in range(4):
        nonz = []
        for r in range(3,-1,-1):
            if grid[r][c] != 0:
                nonz.append(grid[r][c])
        output = []
        score = 0
        if len(nonz) == 4:
            if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0] 
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            elif nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
                output.append(nonz[3])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
                output.append(nonz[3])
            elif nonz[2] == nonz[3]:
                output.append(nonz[0])
                output.append(nonz[1])
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            else:
                output = nonz
        elif len(nonz) == 3:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
            else:
                output = nonz
        elif len(nonz) == 2:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
            else:
                output = nonz
        elif len(nonz) == 1:
            output = nonz
        for r in range(len(output)):
            mat[3-r][c] = output[r]
        while len(output) < 4:
            mat[3-len(output)][c] = 0
            output.append(0)
    return mat
    
def aboard(grid):
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for r in range(4):
        nonz = []
        for c in range(4):
            if grid[r][c] != 0:
                nonz.append(grid[r][c])
        output = []
        score = 0
        if len(nonz) == 4:
            if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0] 
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            elif nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
                output.append(nonz[3])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
                output.append(nonz[3])
            elif nonz[2] == nonz[3]:
                output.append(nonz[0])
                output.append(nonz[1])
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            else:
                output = nonz
        elif len(nonz) == 3:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
            else:
                output = nonz
        elif len(nonz) == 2:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
            else:
                output = nonz
        elif len(nonz) == 1:
            output = nonz
        for c in range(len(output)):
            mat[r][c] = output[c]
        while len(output) < 4:
            mat[r][len(output)] = 0
            output.append(0)
    return mat
  
def dboard(grid):
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for r in range(4):
        nonz = []
        for c in range(3,-1,-1):
            if grid[r][c] != 0:
                nonz.append(grid[r][c])
        output = []
        score = 0
        if len(nonz) == 4:
            if nonz[0] == nonz[1] and nonz[2] == nonz[3]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0] 
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            elif nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
                output.append(nonz[3])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
                output.append(nonz[3])
            elif nonz[2] == nonz[3]:
                output.append(nonz[0])
                output.append(nonz[1])
                output.append(2 * nonz[2])
                score += 2 * nonz[2]
            else:
                output = nonz
        elif len(nonz) == 3:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
                output.append(nonz[2])
            elif nonz[1] == nonz[2]:
                output.append(nonz[0])
                output.append(2 * nonz[1])
                score += 2 * nonz[1]
            else:
                output = nonz
        elif len(nonz) == 2:
            if nonz[0] == nonz[1]:
                output.append(2 * nonz[0])
                score += 2 * nonz[0]
            else:
                output = nonz
        elif len(nonz) == 1:
            output = nonz
        for c in range(len(output)):
            mat[r][3-c] = output[c]
        while len(output) < 4:
            mat[r][3-len(output)] = 0
            output.append(0)
    return mat

def scoringtest():
    game = start(True)

'''def check_rat(grid):
    last = 2**18
    for r in range(4):
        if r % 2 == 0:
            for c in range(4):
                if grid[r][c] > 2*last:
                    if c == 0:
                        True,grid[r-1][c],r-1,c
                    else:
                        return True,grid[r][c-1],r,c-1
                elif grid[r][c] == 0:
                    return False,grid[r][c],r,c
                last = grid[r][c]
        elif r % 2 == 1:
            for c in range(3,-1,-1):
                if grid[r][c] > 2*last:
                    if c == 3:
                        return True,grid[r-1][c],r-1,c
                    else:
                        return True,grid[r][c+1],r,c+1
                elif grid[r][c] == 0:
                    return False,grid[r][c],r,c
                last = grid[r][c]
    return False,grid[r][c],r,c'''
    
'''def ratscoring(board,ratval,ratr,ratc):
    #scoring v1
    #print(board)
    tiles = gettiles(board)
    score = 0
    box= -1
    for r in range(4):
        if r % 2 == 0:
            for c in range(4):
                box +=1
                if c == ratc and r == ratr and board[r][c] == 2*ratval:
                    score += math.exp(-box) * board[r][c]*4
                
                if board[r][c] == sorted(tiles.keys(),reverse = True)[0]:
                    score += math.exp(-box) * board[r][c]
                elif board[r][c] != 0:
                    score += math.exp(-2*box) * board[r][c]    
                if board[r][c] != 0:
                    tiles[board[r][c]] -= 1
                    if tiles[board[r][c]] == 0:
                        tiles.pop(board[r][c])
                        if len(tiles) == 0:
                            return score
        elif r % 2 == 1:
            for c in range(3,-1,-1):
                box +=1
                if c == ratc and r == ratr and board[r][c] == 2*ratval:
                    score += math.exp(-box) * board[r][c]*4
                if board[r][c] == sorted(tiles.keys(),reverse = True)[0]:
                    score += math.exp(-box) * board[r][c]
                elif board[r][c] != 0:
                    score += math.exp(-2*box) * board[r][c]
                if board[r][c] != 0:
                    tiles[board[r][c]] -= 1
                    if tiles[board[r][c]] == 0:
                        tiles.pop(board[r][c])
                        if len(tiles) == 0:
                            return score
    return score'''

'''v0
            points = []
            points.append(game.w()[1])
            points.append(game.a()[1])
            points.append(game.s()[1])
            points.append(game.d()[1])
            m = max(points)
            if p:
                input()
            for i in range(len(points)):
                if game.w()[0] != game.grid:
                    game.up(p)
                    break
                if points[i] == m:
                    if i == 0 and game.w()[0] != game.grid:
                        game.up(p)
                        break
                    elif i == 1 and game.a()[0] != game.grid:
                        game.left(p)
                        break
                    elif i == 3 and game.d()[0] != game.grid:
                        game.right(p)
                        break
                    elif i == 2 and game.s()[0] != game.grid:
                        game.down(p)
                        break'''    

'''#start v1
            points = {}
            if check:
                print("w")
            if game.w()[0] != game.grid:
                points["up"] = scoring(game.w()[0])
            if check:
                print("a")
            if game.a()[0] != game.grid:
                points["left"] = scoring(game.a()[0])
            if check:
                print("s")
            if game.s()[0] != game.grid:
                points["down"] = scoring(game.s()[0])
            if check:
                print("d")
            if game.d()[0] != game.grid:
                points["right"] = scoring(game.d()[0])
            for val in sorted(points.values(),reverse = True):
                 if p:
                     for key in points.keys():
                        if points[key] == val:
                            print(key,"=\t",points[key])
                            break
            
            if p:
                input()
            m = max(points.values())
            if "up" in points and m == points["up"]:
                game.up(p)     
            elif "left" in points and m == points["left"]:
                game.left(p)
            elif "down" in points and m == points["down"]:
                game.down(p) 
            elif "right" in points and m == points["right"]:
                game.right(p)
            #end v1'''
#player(start(True))     
reallysmartgoatedaisupercomputer()
'''a = [16,8,0,4]
b = [0,0,0,2]
c = [0,0,2,0]
d = [0,0,2,0]
print(scoring([a,b,c,d]))'''

'''#start v2!
                points = {}
                if check:
                    print("w")
                if wboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            w = wboard(game.grid)
                            if w[r][c] == 0:
                                w[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*scoring(wboard(w)))
                                two.append(.9*scoring(aboard(w)))
                                two.append(.9*scoring(sboard(w)))
                                two.append(.9*scoring(dboard(w)))
                                w[r][c] = 4
                                four.append(.1*scoring(wboard(w)))
                                four.append(.1*scoring(aboard(w)))
                                four.append(.1*scoring(sboard(w)))
                                four.append(.1*scoring(dboard(w)))
                                best.append(max(two))
                                best.append(max(four))
                    points["up"] = 2*sum(best)/len(best)
                if check:
                    print("a")
                if aboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            a = aboard(game.grid)
                            if a[r][c] == 0:
                                a[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*scoring(wboard(a)))
                                two.append(.9*scoring(aboard(a)))
                                two.append(.9*scoring(sboard(a)))
                                two.append(.9*scoring(dboard(a)))
                                a[r][c] = 4
                                four.append(.1*scoring(wboard(a)))
                                four.append(.1*scoring(aboard(a)))
                                four.append(.1*scoring(sboard(a)))
                                four.append(.1*scoring(dboard(a)))
                                best.append(max(two))
                                best.append(max(four))
                    points["left"] = 2*sum(best)/len(best)
                if check:
                    print("s")
                if sboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            s = sboard(game.grid)
                            if s[r][c] == 0:
                                s[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*scoring(wboard(s)))
                                two.append(.9*scoring(aboard(s)))
                                two.append(.9*scoring(sboard(s)))
                                two.append(.9*scoring(dboard(s)))
                                s[r][c] = 4
                                four.append(.1*scoring(wboard(s)))
                                four.append(.1*scoring(aboard(s)))
                                four.append(.1*scoring(sboard(s)))
                                four.append(.1*scoring(dboard(s)))
                                best.append(max(two))
                                best.append(max(four))
                    points["down"] = 2*sum(best)/len(best)
                if check:
                    print("d")
                if dboard(game.grid) != game.grid:
                    best = []
                    for r in range(4):
                        for c in range(4):
                            d = dboard(game.grid)
                            if d[r][c] == 0:
                                d[r][c] = 2
                                two = []
                                four = []
                                two.append(.9*scoring(wboard(d)))
                                two.append(.9*scoring(aboard(d)))
                                two.append(.9*scoring(sboard(d)))
                                two.append(.9*scoring(dboard(d)))
                                d[r][c] = 4
                                four.append(.1*scoring(wboard(d)))
                                four.append(.1*scoring(aboard(d)))
                                four.append(.1*scoring(sboard(d)))
                                four.append(.1*scoring(dboard(d)))
                                best.append(max(two))
                                best.append(max(four))
                    points["right"] = 2*sum(best)/len(best)
                for val in sorted(points.values(),reverse = True):
                     if p:
                         for key in points.keys():
                            break
                            if points[key] == val:
                                print(key,"=\t",points[key])
                                break
                
                if p:
                    input()
                    #pass
                m = max(points.values())
                if "up" in points and m == points["up"]:
                    game.up(p)     
                elif "left" in points and m == points["left"]:
                    game.left(p)
                elif "down" in points and m == points["down"]:
                    game.down(p) 
                elif "right" in points and m == points["right"]:
                    game.right(p)
                #end v2!'''