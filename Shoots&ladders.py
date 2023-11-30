import random
board = [
    38,2,3,14,5,6,7,8,31,10,
    11,12,13,14,15,6,17,18,19,20,
    42,22,23,24,25,26,27,84,29,30,
    31,32,33,34,35,44,37,38,39,40,
    41,42,43,44,45,46,47,26,11,50,
    67,52,53,54,55,53,57,58,59,60,
    61,19,63,64,65,66,67,68,69,70,
    91,72,73,74,75,76,77,78,79,100,
    81,82,83,84,85,86,24,88,89,90,
    91,92,73,94,75,96,97,78,99,100
]
numplayers = 3
times = 10000

for numplayers in range(1,101):
    tot = 0
    for n in range(times):
        #print(n)
        players = []#the first nums is the space num, the second number is the shot count for each player
        for player in range(numplayers):
            players.append([0,0])
        somewon = False
        while not(somewon):
            for player in players:
                roll = random.randint(1,6)
                if player[0] + roll <= 100:
                    if board[player[0] + roll-1] < 100:
                        newspacenum = board[player[0]+roll-1]
                        if newspacenum < player[0]:
                            player[1] += 1
                        player[0] = newspacenum
                    elif board[player[0] + roll - 1] == 100:
                        somewon = True
                        break
        for player in players:
            tot += player[1]
    print(tot/times/numplayers,numplayers)