"""This is a quickly put together tic tac toe program made to practice python. The logic structure
was taken from the Python Online Bootcamp on Udemy"""

import random



def display_board(board):
	""" Displays the current playing board."""
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[1] + "|" + board[2] + "|" + board[3])

def player_input():
	""" Takes input from player."""
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Please choose beween X and O: ")
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    print("Player 1 is " + player1 + " and Player 2 is " + player2)
    return (player1, player2)

def place_marker(board, marker, position):
	"""Places the player's marker on an available position."""
    if marker != 'X' and marker !='O':
        print("You have provided an invalid marker.")
        return None
    elif position not in range(1,10):
        print("You have entered an invalid position.")
        return None
    else:
        board[position] = marker
        return board

def win_check(board, mark):
	"""Check if a player has won the game."""
    if board[1] == mark and board[2] == mark and board[3] == mark: 
        print(mark + ' has won!')
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark: 
        print(mark + ' has won!')
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark: 
        print(mark + ' has won!')
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark: 
        print(mark + ' has won!')
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark: 
        print(mark + ' has won!')
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark: 
        print(mark + ' has won!')
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark: 
        print(mark + ' has won!')
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark: 
        print(mark + ' has won!')
        return True
    else:
        return False
  

def choose_first():
	"""Selects the player that will go first."""
    result = random.randint(0,1)
    print("Player " + str(result + 1) + " will go first!")
    return result

def space_check(board, position):
	"""Checks if the position is available."""
    return board[position] == ' '

def full_board_check(board):
	"""Checks if the board is full."""
    for x in board:
        if x == ' ':
            return False
    print("The board is full!")
    return True

def player_choice(board):
	"""Takes the player's move."""
    choice = ''
    while not choice in range(1,10):
        choice = input("Please select an unoccupied position between 1 and 9 or enter 0 to exit the game:")
        if choice not in '0123456789':
            continue
        else:
            return int(choice)

def replay():
	""" Asks to replay."""
    choice = ''
    while choice != 'y' and choice != 'n':
        choice = input("Do you want to play again? (y/n)")
    return choice == 'y'



print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    board[0] = ''
    players = player_input()
    first = choose_first()
    display_board(board)
    game_on = True
    
    while game_on:
        #Player 1 Turn
        available = False
        choice= ''
        while not available :
            choice = player_choice(board)
            if choice == 0:
                print("You have exited the game.")
                game_on = False
                break
            available = space_check(board,choice)
        if not game_on:
            break
        place_marker(board, players[first], choice)
        display_board(board)
        if win_check(board, players[first]) or full_board_check(board):
            game_on = False
            break
        
        # Player2's turn.
        available = False
        choice = ''
        while not available:
            choice = player_choice(board)
            if choice == 0:
                print("You have exited the game.")
                game_on = False
                break
            available = space_check(board,choice)
        if not game_on:
            break
        place_marker(board, players[(first * -1) +1], choice)
        display_board(board)
        if win_check(board, players[(first * -1) + 1]) or full_board_check(board):
            game_on = False
    if not replay():
        print("Thank you for playing :)")
        break