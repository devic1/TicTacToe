import sys

board = {1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}

def pri():
    for i in range(1,10,3):
        print("{fir} | {sec} | {thi}".format(fir = board[i],sec = board[i+1],thi = board[i+2]))

def isempty(position):
    if board[position] != '_':
        return True
    return False
pri()

def checkdraw():
    for key,values in board:
        if values == '_':
            return False
    return True

def checkwin():
    if board[1]==board[2] and board[1]==board[3] and board[1] != '_':
        return True
    elif board[1]==board[4] and board[1]==board[7] and board[1] != '_':
        return True
    elif board

