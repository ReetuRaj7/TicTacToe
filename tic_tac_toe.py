print(f'\n'*100)


def display_board(board):
    print("-----------------")
    print("|    |     |    |")
    print(f'|  {board[7]} |  {board[8]}  | {board[9]}  |')
    print("|____|_____|____|")
    
    print(f'----------------')
    print("|    |     |    |")
    print(f'|  {board[4]} |  {board[5]}  | {board[6]}  |')
    print("|____|_____|____|")
  
    print(f'----------------')
    print("|    |     |    |")
    print(f'|  {board[1]} |  {board[2]}  | {board[3]}  |')
    print("|____|_____|____|")
    print("-----------------")
    
def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input(f"Player 1: What do you want to take( X or O) \n").upper()
        
        if not (marker == 'X' or marker == 'O'):
            print("ENTER A VALID VALUE( X or Y)")
            continue
        if marker == 'X' :
            print("So the Player 2 gets marker O")
            return ('X','O')
        else:
            print("So the Player 2 gets marker X")
            return ('O','X')


def place_marker(board, marker, position):
    
    board[position] = marker




def win_check(board, mark):
    
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]== mark and board[6] == mark)or
    (board[7]==mark and board[8]== mark and board[9] == mark)or
    (board[1]==mark and board[5]== mark and board[9] == mark)or
    (board[3]==mark and board[5]== mark and board[7] == mark)or
    (board[1]==mark and board[4]== mark and board[7] == mark)or
    (board[2]==mark and board[5]== mark and board[8] == mark)or
    (board[3]==mark and board[6]== mark and board[9] == mark))
    


import random

def choose_first():
    if random.randint(0,1)== 0:
        print("Player 1 go first")
    else:
        print("Player 2 go first")        

        
        
        
        
def space_check(board, position):
    return board[position]== ' '

def fullcheck(board):
    for x in range(1,10):
        if x == ' ':
            return True
        else:
            return False

#Main Game

gameon =  True
print("WELCOME TO TIC TAC TOE GAME")
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

choice1,choice2 = player_input()
print("######")
choose_first()
print("######")
winner = False
while gameon:
    print(f"THE BOARD AS OF NOW LOOKS LIKE \n")
    display_board(board)
    
    
    #CHANCES
    
    while not winner:
        chance1 = 'Y'
        while chance1 not in [1,2]:
            chance1= int(input("WHOSE CHANCE IS IT (1 or 2)"))
            if chance1 not in [1,2]:
                print("NOT A VALID INPUT!!!(1 or 2)")
        print(f"OK!PLAYER {chance1} ")
        position = 'X'
        while position not in [ 1,2,3,4,5,6,7,8,9]:
            position = int(input(f"WHERE ON THE BOARD YOU WANT TO PLACE THE CHOICE \n"))
            if position not in [ 1,2,3,4,5,6,7,8,9]:
                print("PLEASE ENTER ANY VALID VALUE (1-9)")
        if chance1 == 1:
            marker = choice1
        else:
            marker = choice2
        if space_check(board , position):
            
            place_marker(board, marker, position)
        else:
            print(f"THE SPACE ISN'T EMPTY!! \n")
        
        
        print(f'\n'*30)
        print(f"THE BOARD AS OF NOW LOOKS LIKE \n")
        display_board(board)
        winner = win_check(board, marker)
        if winner:
            print("*"*20)
            
            print("*"*20)
            print(f"THE PLAYER {chance1} WINS \n")
            print("*"*20)
            print("*"*20)
            if chance1 == 1:
                print(f'\n')
                print('     **')
                print('    ***')
                print('  ** **')
                print(' **  **')
                print('     **')
                print('     **')
                print('     **')
                print('     **')
                print(f'\n')
            else:
                print(f'\n')
                print('******')
                print('     *')
                print('     *')
                print('******')
                print('*     ')
                print('*     ')
                print('******')
                print(f'\n')
        fc=fullcheck(board)    
        if not(winner and fc):
            print("NO WINNER THE GAME IS DRAWN!!!!")
        
          
            
        
    print(f"DO WANT TO PLAY MORE(YES OR NO)")
    gmode = input(f"\n").lower()
    if gmode == 'yes' or gmode.startswith('y'):
        gameon = True



def full_board_check(board):
    return ' ' not in board



def player_choice(board):
    next_pos = input('At what position do you want ot fill in:')
    
    if next_pos not in ['1','2','3','4','5','6','7','8','9']:
            print("Please enter a choice between 1-9")
    
    pos_check = space_check(board, next_pos)
    if pos_check:
        print("OK CHOICE REGISTERED")
    else:
        print("CHOICE COULDN'T BE REGISTERED AS POSITION FILLED ALREADY") 
        


def replay():
    choice = 'Not'
    
    while choice not in ['Y','N']:
        
        
        choice =  input("PLAY MORE(Y or N)").upper()
        
        if choice == 'Y':
            return True
        else:
            return False
    
    

        
        
        
        
        
        
        
        
        
        
