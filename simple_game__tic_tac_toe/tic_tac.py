import random


board=[' ']*10
computer='X'
human='0'

def display_board(board):
    print(f'{board[1]}  |  {board[2]} |  {board[3]}')
    print(f'{board[4]}  |  {board[5]} |  {board[6]}')
    print(f'{board[7]}  |  {board[8]} |  {board[9]}')
    print('_'*30)
    
    
    
def check_win():
    if board[1]==board[2]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    elif board[1]==board[5]==board[9] and board[1]!=' ':
        return True
    elif board[7]==board[5]==board[3] and board[7]!=' ':
        return True
    else:
        return False
def check_draw():
    if board.count(' ')<2: #nammude list il 10 space und  9 ennam use cheyyunullu adhyathe index ullath null aahnu so athu koodi include cheyyanam
        return True
    else:
        return False


#oru position ilottu  letter insert cheyyumbol for eg 0 insert cheyyumbol
#1adhyam space indonu nokkanam,
#2.already avide 0 insert chethitindnkil avide insert cheyyan patilla
#3.position available aahno ennu nokanm

def is_available(pos):
    return True if board[pos]==' ' else False

def insert(letter,pos):
    if is_available(pos):
        board[pos]=letter
        display_board(board)
        if check_win():
            if letter =='X':
                print("computer wins")
                exit()
            else:
                print("human wins")
                exit()
        if check_draw():
            print("draw")
    else:
        if letter=='0':
            pos=int(input("Not free please enter a new position"))
        else:
            pos=random.randint(1,9)
        insert(letter,pos)








def human_move(letter):
    pos=int(input("enter a number"))
    insert(letter,pos)
def computer_move(letter):
    pos=random.randint(1,9)
    insert(letter,pos)

while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)

