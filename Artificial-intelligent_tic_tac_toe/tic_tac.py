import random


board=[' ']*10
computer='X'
human='0'

def display_board(board):
    print(f'{board[1]}  |  {board[2]} |  {board[3]}')
    print(f'{board[4]}  |  {board[5]} |  {board[6]}')
    print(f'{board[7]}  |  {board[8]} |  {board[9]}')
    print('_'*10)
    
    
    
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

def is_win(letter):
    if board[1]==board[2]==board[3] and board[1]==letter:
        return True
    elif board[4]==board[5]==board[6] and board[4]==letter:
        return True
    elif board[7]==board[8]==board[9] and board[7]==letter:
        return True
    elif board[1]==board[4]==board[7] and board[1]==letter:
        return True
    elif board[2]==board[5]==board[8] and board[2]==letter:
        return True
    elif board[1]==board[5]==board[9] and board[1]==letter:
        return True
    elif board[7]==board[5]==board[3] and board[7]==letter:
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
            exit()

    else:

        pos=int(input("Not free please enter a new position"))


        insert(letter,pos)








def human_move(letter):
    pos=int(input("enter a number"))
    insert(letter,pos)
def computer_move(letter):
    best_score=-100
    best_pos=0
    for index in range(1,len(board)):
        if is_available(index):
            board[index]=letter
            score=minimax(board,False)
            board[index]=" "
            if score>best_score:
                best_score=score
                best_pos=index
    insert(letter,best_pos)
    return
def minimax(board,is_maximizing):
    if is_win(computer):
        return 10
    elif is_win(human):
        return -10
    elif check_draw():
        return 0
    if is_maximizing:
        best_score = 100

        for index in range(1, len(board)):
            if is_available(index):
                board[index] = computer
                score = minimax(board, False)
                board[index] = " "
                best_score=max(best_score,score)
        return best_score

    else:
        best_score = 100

        for index in range(1, len(board)):
            if is_available(index):
                board[index] = human
                score = minimax(board, True)
                board[index] = " "
                best_score=min(best_score,score)
        return best_score



#main loop
while not check_win():
    display_board(board)
    computer_move(computer)
    human_move(human)
