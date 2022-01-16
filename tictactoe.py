import sys

board = {1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}

def pri():
    for i in range(1,10,3):
        print("{fir} | {sec} | {thi}".format(fir = board[i],sec = board[i+1],thi = board[i+2]))

def isempty(position):
    if board[position] == '_':
        return True
    return False

def checkdraw():
    for key in board:
        if board[key] == '_':
            return False
    return True

def checkwin():
    if board[1]==board[2] and board[1]==board[3] and board[1] != '_':
        return True
    elif board[4]==board[5] and board[4]==board[6] and board[4] != '_':
        return True
    elif board[7]==board[8] and board[7]==board[9] and board[7] != '_':
        return True
    elif board[1]==board[4] and board[1]==board[7] and board[1] != '_':
        return True
    elif board[2]==board[5] and board[2]==board[8] and board[2] != '_':
        return True
    elif board[3]==board[6] and board[3]==board[9] and board[3] != '_':
        return True
    elif board[1] == board[4] and board[1] == board[9] and board[1] != '_':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != '_':
        return True
    else:
        return False

def ins(letter,position):
    if isempty(position):
        board[position] = letter
        pri()
        if checkdraw():
            print("Draw")
            exit()
        if checkwin():
            if letter == 'x':
                print("X wins ")
                exit()
            else:
                print("O wins ")
                exit()
            return
    else:
        print("Full")


pri()
for i in range(3):
    g = int(input("Enter : "))
    p = input("Enter pos : ")
    ins(p,g)



