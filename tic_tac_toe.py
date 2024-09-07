# Author: Silas Accles
# Created: June 6, 2024
# Last Modified: June 6, 2024

import random
import time

board = [" " for field in range(9)] 

def display_board():
    """
    A function that displays the tic tac toe board.
    """
    # ASCII representation of the tic tac toe board at any time.
    print(f"""
    {board[0]}|{board[1]}|{board[2]}
    -----
    {board[3]}|{board[4]}|{board[5]}
    -----
    {board[6]}|{board[7]}|{board[8]}
""")
    
def computer_make_move():
    """
    A function that randomly makes a move on the tic tac toe board, 
    providing the computer side of the game decisions.
    """
    computer_move = random.choice(range(9))
    return computer_move

def user_make_move():
    """
    A function that asks the user to make a move 
    on the tic tac toe board and stores the user's move.
    """
    user_move = int(input("Choose a number from 1 to 9: "))
    return (user_move - 1)

def validate_computer_move(computer_move):
    """
    A function that validates the computer's moves, 
    making sure that used fields are not overwritten.
    """
    # If the tic tac toe field is blank, return true.
    if board[computer_move] == " ":
        return True
    # If the tic tac toe field is already filled, return false. 
    elif (board[computer_move] == "x") or (board[computer_move] == "o"):
        return False
    
def validate_user_move(user_move):
    """
    A function that validates the user's moves, 
    making sure that used fields are not overwritten 
    and that only valid input is accepted by the program.
    """
    # If the user's move is in the proper range 
    # and the tic tac toe field is blank, return true.
    if (user_move in range(9)) and (board[user_move] == " "):
        return True
    # If the user's move is not in the proper range, return false. 
    elif user_move not in range(9):
        print("Invalid move! Try again.")
        return False
    # If the user's move is in the proper range 
    # but the tic tac toe field has already been filled, return false.
    elif (board[user_move] == "x") or (board[user_move] == "o"):
        print("Field already taken. Choose another number.")
        return False
    
def update_board_computer(computer_move):
    """
    A function that updates the board with the computer's move.
    """
    # Keep making a new move until the move is valid.
    while validate_computer_move(computer_move) == False:
        computer_move = computer_make_move()
    board[computer_move] = "x"

def update_board_user(user_move):
    """
    A function that updates the board with the user's move.
    """
    # Keep asking for a new move until the move is valid.
    while validate_user_move(user_move) == False:
        user_move = user_make_move()
    board[user_move] = "o"

def get_game_status():
    """
    """
    game_status = ""

    # If the computer has three x's in a row or other combination, 
    # declare a computer victory.
    if board[0] == board[1] == board[2] == "x":
        game_status = "computer victory"
    elif board[3] == board[4] == board[5] == "x":
        game_status = "computer victory"
    elif board[6] == board[7] == board[8] == "x":
        game_status = "computer victory"
    elif board[0] == board[3] == board[6] == "x":
        game_status = "computer victory"
    elif board[1] == board[4] == board[7] == "x":
        game_status = "computer victory"
    elif board[2] == board[5] == board[8] == "x":
        game_status = "computer victory"
    elif board[0] == board[4] == board[8] == "x":
        game_status = "computer victory"
    elif board[6] == board[4] == board[2] == "x":
        game_status = "computer victory"

    # If the user has three o's in a row or other combination, 
    # declare a user victory.
    if board[0] == board[1] == board[2] == "o":
        game_status = "user victory"
    elif board[3] == board[4] == board[5] == "o":
        game_status = "user victory"
    elif board[6] == board[7] == board[8] == "o":
        game_status = "user victory"
    elif board[0] == board[3] == board[6] == "o":
        game_status = "user victory"
    elif board[1] == board[4] == board[7] == "o":
        game_status = "user victory"
    elif board[2] == board[5] == board[8] == "o":
        game_status = "user victory"
    elif board[0] == board[4] == board[8] == "o":
        game_status = "user victory"
    elif board[6] == board[4] == board[2] == "o":
        game_status = "user victory"

    # If no fields remain and neither the user or the computer 
    # have three x's or o's in a row or other combination, declare a draw.
    elif (" " not in board) and (game_status != "computer victory") and (game_status!= "user victory"):
        game_status = "no victory"
    
    return game_status

instructions = """
|---------------------------------------------------------------------|
|How To Play:                                                         |
|                                                                     |
| - When the game starts, the board is displayed.                     |
| - The computer then makes a move.                                   |
| - Once the computer has made its move, you may make your move.      |
| - When that time comes along, choose a number from 1 to 9.          |
| - This number corresponds with the fields of the tic tac toe board, |
|   which are numbered left to right, top to bottom.                  |
| - To win, get three o's in a row on the tic tac toe board.          |
|                                                                     |  
|Example:                                                             |
|                                                                     |
|If a player wanted to choose the field in the center of the          |
|tic tac toe board, they would choose the number 5.                   |
|                                                                     |
|Good luck!                                                           |
|---------------------------------------------------------------------|
"""
closing_message = "Thanks for playing!"
print("--------------------")
print("Tic ... Tac ... Toe!")
print("--------------------")
print(f"\n{instructions}")
print("Game Board:")
display_board()
time.sleep(2)

# Initiate main program loop.
while True:
    computer_move = computer_make_move()
    update_board_computer(computer_move)
    print("Computer Move:")
    display_board()
    time.sleep(2)
    game_status = get_game_status()
    if game_status == "computer victory":
        print("I win!")
        print(closing_message)
        break
    elif game_status == "user victory":
        print("You win!")
        print(closing_message)
        break
    elif game_status == "no victory":
        print("The game ended, but neither of us won.")
        print(closing_message)
        break
    user_move = user_make_move()
    update_board_user(user_move)
    print("User Move:")
    display_board()
    time.sleep(2)
    game_status = get_game_status()
    if game_status == "computer victory":
        print("I win!")
        print(closing_message)
        break
    elif game_status == "user victory":
        print("You win!")
        print(closing_message)
        break
    elif game_status == "no victory":
        print("The game ended, but neither of us won.")
        print(closing_message)
        break