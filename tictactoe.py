import sys
import random


print("\t\tTIC-TAC-TOE AI\t\t\n")
board = {1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
player = input("choose a player : ")
if player == 'X':
    bot = 'O'
else:
    bot = 'X'
ra = int(input("Heads (1) or Tails (2): "))
s = random.randint(1,2)
print("You Won \n " if ra == s else "You Lost \n")

def pri():
    for i in range(1,10,3):
        print("{fir} | {sec} | {thi}".format(fir = board[i],sec = board[i+1],thi = board[i+2]))
    print("\n")

def isempty(position):
    if board[position] == '_':
        return True
    return False

def checkdraw():
    for key in board:
        if board[key] == '_':
            return False
    return True

def checkwin(mark):
    emp = '_'
    if board[1]==board[2] and board[1]==board[3] and board[1] == mark and board[1] != emp:
        return True
    elif board[4]==board[5] and board[4]==board[6] and board[4] == mark and board[4] != emp:
        return True
    elif board[7]==board[8] and board[7]==board[9] and board[7] == mark and board[7] != emp:
        return True
    elif board[1]==board[4] and board[1]==board[7] and board[1] == mark and board[1] != emp:
        return True
    elif board[2]==board[5] and board[2]==board[8] and board[2] == mark and board[2] != emp:
        return True
    elif board[3]==board[6] and board[3]==board[9] and board[3] == mark and board[3] != emp:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark and board[1] != emp:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark and board[3] != emp:
        return True
    else:
        return False

def playmove():
    pos = int(input("Enter : "))
    ins(player,pos)
    print("\n")

def ins(letter,position):
    if isempty(position):
        board[position] = letter
        pri()
        if checkdraw():
            print("Draw")
            exit()
        if checkwin('X'):
            print("X wins ")
            exit()
        if checkwin('O'):
            print("O wins ")
            exit()
        return
    else:
        playmove()
        print("\n")

def compmove():
    bestscore = -800
    bestmove = 1
    for key in board:
        if(board[key] == '_'):
            board[key] = bot
            score = minimax(board,0,False)
            board[key] = '_'
            if(score > bestscore):
                bestscore = score
                bestmove = key
    ins(bot,bestmove)

def minimax(board,depth,ismax):
    if checkwin(bot):
        return 1
    elif checkwin(player):
        return -1
    elif checkdraw():
        return 0
    else:
        if(ismax):
            bestscore = -800
            for key in board:
                if(board[key] == '_'):
                    board[key] = bot
                    score = minimax(board,depth+1,False)
                    board[key] = '_'
                    bestscore = max(score,bestscore)
            return bestscore
        else:
            bestscore = 800
            for key in board:
                if(board[key] == '_'):
                    board[key] = player
                    score = minimax(board,depth+1,True)
                    board[key] = '_'
                    bestscore = min(score,bestscore)
            return bestscore

while not checkwin('X') or checkwin('O'):
    if(ra == s):
        playmove()
        compmove()
    else:
        compmove()
        playmove()



