import random
import numpy as np
import matplotlib.pyplot as plt
Num_Decks = 4

class hand():
  def __init__(self,card1, card2, can_hit = True, doubled = False):
    self.cards = [card1,card2]
    self.can_hit = can_hit
    self.doubled = doubled
    self.ace_count = 0
    if card1 == 1:
      self.ace_count += 1
    if card2 == 1:
      self.ace_count += 1
    self.value = self.update_val()

  def hit(self,shoe):
    if self.can_hit:
      self.cards.append(shoe[0])
      if shoe[0] == 1:
        self.ace_count += 1
    self.value = self.update_val()

  def double(self, shoe):
    self.hit(self, shoe)
    self.can_hit = False
    self.doubled = True

  def stand(self):
    self.can_hit = False
    self.update_val()

  def update_val(self):
    total = 0
    for card in self.cards:
      if card == 1:
        total +=11
      elif card<11:
        total+=card
      else:
        total += 10
    remaining_aces = self.ace_count
    while total > 21 and remaining_aces > 0:
      remaining_aces -=1
      total -= 10
    return total

  def __repr__(self):
    s = "["
    for card in self.cards:
      s += str(card) + " "
    return s +"]"


def shuffle(num_of_decks):
  shoe = []
  for deck in range(num_of_decks):
    for suit in range(4):
      for num in range(1,14):
        shoe.append(num)
  random.shuffle(shoe)
  return shoe

def rem_cards(num,shoe):
  for card in range(num):
    shoe.pop(0)
  return shoe

def split(player_hand,players_hands,shoe):
  output = []
  for hand1 in players_hands:
    if player_hand == hand1:
      output.append(hand(player_hand.cards[0],shoe[0]))
      output.append(hand(player_hand.cards[1],shoe[1]))
    else:
      output.append(hand1)
  return output

def split_check(player_hands,dealer_hand, shoe):
  deal_val = dealer_hand.cards[0]
  for player_hand in player_hands:
    if player_hand.cards[0] == player_hand.cards[1]:
      val = player_hand.cards[0]
      if val == 8 or val == 1:
        player_hands = split(player_hand,player_hands,shoe)
        player_hand = True
      elif val == 5 or val > 9:
        pass
      elif val == 2 or val == 3:
        if deal_val < 8 and deal_val != 1:
          player_hands = split(player_hand,player_hands,shoe)
          player_hand = True
      elif val == 4:
        if deal_val < 7 and deal_val > 4:
          player_hands = split(player_hand,player_hands,shoe)
          player_hand = True
      elif val == 6:
        if deal_val < 7 and deal_val != 1:
          player_hands = split(player_hand,player_hands,shoe)
          player_hand = True
      elif val == 7:
        if deal_val < 8 and deal_val != 1:
          player_hands = split(player_hand,player_hands,shoe)
          player_hand = True
      elif val == 9:
        if (deal_val < 7 and deal_val>1) or (deal_val > 7 and deal_val < 10):
          player_hands = split(player_hand,player_hands,shoe)
          player_hand = True
  return player_hands

def player_hits(player_hands,dealer_hand, shoe, bal, bet):
  deal_val = dealer_hand.cards[0]
  for han in player_hands:
    while han.can_hit and not(len(dealer_hand.cards) == 2 and dealer_hand.value == 21):
      if not(han.has_ace):
        if han.value < 9:
          han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 9:
          if deal_val >2 and deal_val<7 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 10:
          if deal_val > 1 and deal_val< 10 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 11:
          if bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 12:
          if deal_val > 3 and deal_val< 7:
            han.stand()
          else:
            han.hit(shoe)
            shoe = rem_cards(1, shoe)
        elif han.value > 12 and han.value < 17:
          if deal_val > 1 and deal_val< 7:
            han.stand()
          else:
            han.hit(shoe)
            shoe = rem_cards(1, shoe)
        else:
          han.stand()

      else:
        if han.value < 15:
          if deal_val ==5 or deal_val==6 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 16 or han.value == 15:
          if deal_val >3 and deal_val<7 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 17:
          if deal_val > 2 and deal_val< 7 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.hit(shoe)
          shoe = rem_cards(1, shoe)
        elif han.value == 18:
          if bal >= bet and deal_val >1 and deal_val<7:
            han.hit(shoe)
            bal -= bet
            shoe = rem_cards(1, shoe)
            han.doubled = True
            han.stand()
          elif deal_val > 8 or deal_val == 1:
            han.hit(shoe)
            shoe = rem_cards(1, shoe)
          else:
            han.stand()
        elif han.value == 19:
          if deal_val == 6 and bal >= bet:
            han.hit(shoe)
            bal -= bet
            han.doubled = True
            han.stand()
          else:
            han.stand()
        else:
          han.stand()
  return (player_hands, shoe, bal)

def dealer_hits(dealer_hand, shoe):
  while dealer_hand.value < 17:
    dealer_hand.hit(shoe)
    shoe = rem_cards(1, shoe)
  return (dealer_hand, shoe)

def result(player_hands, dealer_hand):
  results = []
  for han in player_hands:
    if len(han.cards) == 2 and han.value == 21 and not(len(dealer_hand.cards) == 2 and dealer_hand.value == 21):
      results.append((1.5,han.doubled))
    elif len(han.cards) == 2 and han.value == 21:# this is a blackjack push
      results.append((0,han.doubled))
    elif len(dealer_hand.cards) == 2 and dealer_hand.value == 21:
      results.append((-1,han.doubled))
    elif han.value > 21:
      results.append((-1,han.doubled))
    elif dealer_hand.value > 21:
      results.append((1,han.doubled))
    elif han.value < dealer_hand.value:
      results.append((-1,han.doubled))
    elif han.value > dealer_hand.value:
      results.append((1,han.doubled))
    else:
      results.append((0,han.doubled))
  return results

def game(bet, bal):
  shoe = shuffle(Num_Decks)
  dealer_hand = hand(shoe[0],shoe[1])
  player_hands = [hand(shoe[2],shoe[3])]
  shoe = rem_cards(4,shoe)
  if bal >= bet  and not(len(dealer_hand.cards) == 2 and dealer_hand.value == 21):
    player_hands = split_check(player_hands, dealer_hand, shoe)
    if player_hands[0].doubled:
      bal -= bet
      shoe = rem_cards(2,shoe)

  #print(player_hands,dealer_hand)

  data1 = player_hits(player_hands,dealer_hand, shoe, bal, bet)
  player_hands = data1[0]
  shoe = data1[1]
  bal = data1[2]

  data2 = dealer_hits(dealer_hand, shoe)
  dealer_hand = data2[0]
  shoe = data2[1]

  #print(player_hands,dealer_hand,end="\n\n")

  return result(player_hands,dealer_hand)


def bust_chance():
  # the dealer only has a very limited number of possible results (17,18,19,20,21,blackjack, or bust)
  #I want to find the probability of each result with a given displayed card
  bust_chances = []
  for deal in range(1,11):
    bust_chances.append([0,0,0,0,0,0,0])#17,18,19,20,21,bj,bust
    shoes = 100000
    total = 0
    for num in range(shoes):
      shoe = shuffle(Num_Decks)
      shoe.remove(deal)
      random.shuffle(shoe)
      shuffle_time = Num_Decks*52*(1/3 + 5/12 * random.random())
      while len(shoe) > shuffle_time:
        dealer_hand = hand(shoe[0],deal)
        shoe = rem_cards(1,shoe)
        data = dealer_hits(dealer_hand, shoe)
        dealer_hand = data[0]
        shoe = data[1]
        if dealer_hand.value<21:
          bust_chances[deal-1][dealer_hand.value-17] += 1
        elif dealer_hand.value==21:
          if len(dealer_hand.cards) == 2:
            bust_chances[deal-1][5] += 1#bj
          else:
            bust_chances[deal-1][4] += 1#regular 21
        else:
          bust_chances[deal-1][6] += 1#bust
        total += 1
    # print(total)
    for j in range(7):
      bust_chances[deal-1][j] /= total
      
  f=open("BlackJackSimulator/" + str(Num_Decks) + "DealerResults.txt","w")
  lines = ['\t|17\t\t\t|18\t\t\t|19\t\t\t|20\t\t\t|21\t\t\t|BJ\t\t\t|Bust\n']
  round_place = 7
  for i, deal_num in enumerate(bust_chances):
    # for j in range(len(deal_num)):
    #   if deal_num[j] == 0:
    #     output = '0.'
    #     for k in range(round_place):
    #       output += '0'
    #     deal_num[j] = output
    if i == 0:
      lines.append('A\t|' + str(round(deal_num[0],round_place)) +'\t|' + str(round(deal_num[1],round_place)) +'\t|' + str(round(deal_num[2],round_place)) +'\t|' + str(round(deal_num[3],round_place)) +'\t|' + str(round(deal_num[4],round_place)) +'\t|' + str(round(deal_num[5],round_place)) +'\t|' + str(round(deal_num[6],round_place)) +'\n')
    elif i == 9:
      lines.append(str(i+1) + '\t|' + str(round(deal_num[0],round_place)) +'\t|' + str(round(deal_num[1],round_place)) +'\t|' + str(round(deal_num[2],round_place)) +'\t|' + str(round(deal_num[3],round_place)) +'\t|' + str(round(deal_num[4],round_place)) +'\t|' + str(round(deal_num[5],round_place)) +'\t|' + str(round(deal_num[6],round_place)) +'\n')
    else:
      lines.append(str(i+1) + '\t|' + str(round(deal_num[0],round_place)) +'\t|' + str(round(deal_num[1],round_place)) +'\t|' + str(round(deal_num[2],round_place)) +'\t|' + str(round(deal_num[3],round_place)) +'\t|' + str(round(deal_num[4],round_place)) +'\t|' + str(round(deal_num[5],round_place)) +'\t\t|' + str(round(deal_num[6],round_place)) +'\n')
  f.writelines(lines)
  f.close()


  f=open("BlackJackSimulator/" + str(Num_Decks) + "ProbData.txt","w")
  lines = []
  for i, deal_num in enumerate(bust_chances):
    lines.append('')
    for j in range(len(deal_num)):
      lines[i] += str(deal_num[j])
      if j != len(deal_num) - 1:
        lines[i] += ','
    lines[i] += '\n'
  f.writelines(lines)
  f.close()
  # print(bust_chances)


  r = np.arange(7)
  width = 1/14
    
  for i, deal_num in enumerate(bust_chances):
    plt.bar(r + width*i, deal_num, width)

  plt.legend(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10'],ncol = 10,fontsize = 6)
  plt.xticks(r+.3,['17', '18', '19','20', '21', 'BJ','Bust'])
  plt.xlabel('Outcome')
  plt.ylabel('Probability')
  plt.title('Dealer Outcomes for '+ str(Num_Decks) + ' Decks')
  plt.show()


def basic_strat_table():
  trial_data = [[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]]]
  hard_table = [[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[],[]]]
  for fir in range(2,14):#no aces
    print(fir)
    for sec in range(2,14):
      print(sec)
      for deal in range(1,11):
        for types in range(2):
          bal = 10000
          bet = 1
          count = 20
          total = 0
          roi_avg = 0
          for num in range(count):
            shoe = shuffle(Num_Decks)
            shoe.remove(fir)
            shoe.remove(sec)
            shoe.remove(deal)
            random.shuffle(shoe)#ensure random dealing
            dealer_hand = hand(shoe[0],deal)
            player_hand = hand(fir,sec)
            shoe = rem_cards(1,shoe)
            shuffle_time = Num_Decks*52*(1/3 + 5/12 * random.random())#this is a coeiffent randomly between 1/3 and 3/4
            # print(shuffle_time)
            while len(shoe) > shuffle_time and types == 0:
              if types == 0:
                player_hand.hit(shoe)
                # player_hand.stand()
                shoe = rem_cards(1, shoe)
              elif types == 1:
                pass #not doing anything = standing but faster
                # player_hand.stand() #
              elif types == 2:
                data1 = player_hits(player_hand,dealer_hand, shoe, bal, bet)
                player_hand = data1[0]
                shoe = data1[1]
                          
              data2 = dealer_hits(dealer_hand, shoe)
              dealer_hand = data2[0]
              shoe = data2[1]
            
              roi_avg = (total * roi_avg + result([player_hand],dealer_hand)[0][0]) / (total + 1)
              total += 1
              # print(total,len(shoe))
              # print(rois,len(shoe))
          trial_data[21-(fir+sec)][deal-1].append((roi_avg,types))
  
  print(trial_data)
  input()
  for i,hand_val in enumerate(trial_data):
    for j,deal_val in enumerate(hand_val):
      for data in deal_val:
        hard_table[i][j].append(data[0])

def single_hit():
  trial_data = []
  for val in range(4,21): # hand starting values smallest is 4 largest is 20.
    trial_data.append([0,0,0,0,0,0,0])# each starting value [4-16,17,18,19,20,21,bust]
  for fir in range(2,14):#no aces
    for sec in range(2,14):
      count = 20
      for num in range(count):
        shoe = shuffle(Num_Decks)
        shoe.remove(fir)
        shoe.remove(sec)
        random.shuffle(shoe)#ensure random dealing
        player_hand = hand(fir,sec)
        og_val = player_hand.value
        shoe = rem_cards(1,shoe)
        shuffle_time = Num_Decks*52*(1/3 + 5/12 * random.random())
        while len(shoe) > shuffle_time:
          player_hand = hand(fir,sec)
          player_hand.hit(shoe)
          shoe = rem_cards(1, shoe)
          if player_hand.value<17:
            trial_data[og_val-4][0] += 1
          elif player_hand.value<=21:
            trial_data[og_val-4][player_hand.value-16] += 1
          else:
            trial_data[og_val-4][6] += 1
  for i, starting_val in enumerate(trial_data):
    total = 0
    for num in starting_val:
      total += num
    for j in range(len(starting_val)):
      trial_data[i][j] /= total

  f = open("BlackJackSimulator/" + str(Num_Decks) + "ProbData.txt", "r")
  lines = []
  for line in f:
    lines.append(line.strip().split(","))
  f.close()
  deal_probs = []
  for i, line in enumerate(lines):
    deal_probs.append([])
    for val in line:
      deal_probs[i].append(float(val))

  print('Player probs',trial_data)
  print()
  print('Dealer probs',deal_probs)
  input()
  winning_chances = []    
  for i, starting_val in enumerate(trial_data):
    winning_chances.append([])
    for j, play_outcome in enumerate(starting_val):
      winning_chances[i].append([0,0])#[expected ROI if stand, expected ROI if hit once] for a certain player starting value
      for m, deal_val in enumerate(deal_probs):
        winning_chances
        for deal_outcome in deal_val:
          winning_chances[i][1]

'''
            for stat in stats:
              if stat[0] == "Win":
                win_count += 1
                total += 1
              elif stat[0] == "Loss":
                loss_count += 1
                total += 1
              else:
                push_count += 1
                total += 1
          if types == 1:
            print("Stand:")
          elif types == 2:
            print("Hit:")
          elif types == 0:
            print("Double:")
          print("Win Percent =",win_count*100/total)
          print("Loss Percent =",loss_count*100/total)
          print("Push Percent =",push_count*100/total)
          print("ROI Score: {}%".format(win_count*100/total - loss_count*100/total))
          print()
          '''

# basic_strat_table()

# bust_chance()

single_hit()

'''
bet = 50000
balt = 2000000
max_bal = 0
earnings = 0
bj_count = 0
win_count = 0
loss_count = 0
push_count = 0
total = 0
highs = 0
mades = 0
for nu in range(10000):
  made_it = False
  balt = 1000000
  max_bal = 0
  total = 0
  for num in range(100000):
    stats = game(bet,balt)
    for stat in stats:
      if stat[0] == "Blackjack":
        if not(stat[1]):
          earnings += bet*3/2
          balt += bet*3/2
        bj_count += 1
        win_count += 1
        total += 1
      elif stat[0] == "Win":
        if stat[1]:
          earnings += bet*2
          balt += bet*2
        else:
          earnings += bet
          balt += bet
        win_count += 1
        total += 1
      elif stat[0] == "Loss":
        if stat[1]:
          earnings -= bet*2
          balt -= bet*2
        else:
          earnings -= bet
          balt -= bet
        loss_count += 1
        total += 1
      else:
        push_count += 1
        total += 1
    if balt < bet:
      break
    if balt > max_bal:
      max_bal = balt
    if balt >= 1500000:
      made_it = True
      break
  highs += max_bal
  if made_it:
    mades += 1
  print(mades)
  

print("Gross Earnings =", earnings)
print("Win Percent =",win_count*100/total)
print("Loss Percent =",loss_count*100/total)
print("Push Percent =",push_count*100/total)
print("BlackJacks =",bj_count)
print("Winnings per Hand =",earnings/total)
print("Total =",total)
#print("Higest =",max_bal)
print("High =", highs/total)
print("Made it to 1.5mil {}%".format(mades/100))'''