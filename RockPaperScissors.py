#Blake Wendland
#wendl198
#Exam 1
#Question 3

import random

def RockPaperScissors(N):
  ai1_wins = 0
  ai1_loses = 0
  ai1_draws = 0

  ai2_wins = 0
  ai2_loses = 0
  ai2_draws = 0

  ai3_wins = 0
  ai3_loses = 0
  ai3_draws = 0

  for game in range(N):
    ai1_choice = random.randint(1, 3)
    ai2_choice = random.randint(1, 3)
    #paper is 1, scissors is 2, rock is 3
    ai3_choice = random.randint(1, 4)
    #paper is 1, scissors is 2, rock is 3 and 4
    #Note, this makes rock 50%, paper 25% and scissors 25%

    game1 = gameplay(ai1_choice, ai2_choice)
    game2 = gameplay(ai3_choice, ai2_choice)
    game3 = gameplay(ai1_choice, ai3_choice)

    if game1 == ai1_choice:
      ai1_wins += 1
      ai2_loses += 1
    elif game1 == ai2_choice:
      ai2_wins += 1
      ai1_loses += 1
    else:
      ai1_draws += 1
      ai2_draws += 1

    if game2 == ai3_choice:
      ai3_wins += 1
      ai2_loses += 1
    elif game2 == ai2_choice:
      ai2_wins += 1
      ai3_loses += 1
    else:
      ai3_draws += 1
      ai2_draws += 1

    if game3 == ai1_choice:
      ai1_wins += 1
      ai3_loses += 1
    elif game3 == ai3_choice:
      ai3_wins += 1
      ai1_loses += 1
    else:
      ai1_draws += 1
      ai3_draws += 1


  print("Random Player 1:\nWins:{} Loses:{} Draws:{}\n".format(ai1_wins, ai1_loses, ai1_draws))
  print("Random Player 2:\nWins:{} Loses:{} Draws:{}\n".format(ai2_wins, ai2_loses, ai2_draws))
  print("Rock Biased Player:\nWins:{} Loses:{} Draws:{}".format(ai3_wins, ai3_loses, ai3_draws))
    

def gameplay(player1_choice, player2_choice):
  if player1_choice == player2_choice or player1_choice +player2_choice == 7:
    return None
    #this is if it is a draw
    #The or statment, is for the unique case if a3 picks 4 for a rock 
    #and the ai also picks rock

  #p1 has paper
  if player1_choice == 1:
    if player2_choice == 2:
      return player2_choice
      #scissors beat paper
    else:
      return player1_choice
      #paper beat rock

  #p1 has scissors
  elif player1_choice == 2:
    if player2_choice == 1:
      return player1_choice
      #scissors beat paper
    else:
      return player2_choice
      #rock beat scissors

  #p1 has rock
  else:
    if player2_choice == 2:
      return player1_choice
      #rock beat scissors
    else:
      return player2_choice
      #paper beat rock

def main():
  RockPaperScissors(10000000)

if __name__ == "__main__":
  main()
