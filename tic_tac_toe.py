# Author: Silas Accles
# Created: June 6, 2024
# Last Modified: January 12, 2024

from random import choice
from time import sleep

# Initialize the one-dimensional array that represents the tic tac toe board.
game_board = [" " for field in range(9)]


def display_game_board():
    """Display an ASCII representation of the tic tac toe board."""

    # Real-time, ASCII representation of the tic tac toe board.
    print(
        f"""
    {game_board[0]}|{game_board[1]}|{game_board[2]}
    -----
    {game_board[3]}|{game_board[4]}|{game_board[5]}
    -----
    {game_board[6]}|{game_board[7]}|{game_board[8]}
    """
    )


def get_computer_move():
    """
    Randomly choose and return a field on the tic tac toe board
    for the computer to occupy.
    """
    computer_move = choice(range(9))

    return computer_move


def get_user_move():
    """
    Prompt the user to choose a field on the tic tac toe board
    to occupy and return the field.
    """
    user_move = int(input("Choose a number from 1 to 9: "))

    return (user_move - 1)


def validate_computer_move(computer_move):
    """
    Return True if the computer's move is valid or 
    False if the computer's move is invalid.
    
    Arguments:  
        computer_move (int): the computer's chosen move

    Returns:
        True if the computer's move is valid or False
        if the computer's move is invalid
    """

    # If the field on the tic tac toe board is empty,
    # return True.
    # Otherwise, if the field on the tic tac toe board
    # has already been filled, return False.
    if game_board[computer_move] == " ":
        return True
    elif (game_board[computer_move] == "x") or (
        game_board[computer_move] == "o"
    ):
        return False


def validate_user_move(user_move):
    """
    Return True if the user's move is valid or 
    False if the user's move is invalid.
    
    Arguments:  
        user_move (int): the user's chosen move

    Returns:
        True if the user's move is valid or False
        if the user's move is invalid
    """

    # If the user's move is in the proper range and the tic tac toe field
    # is empty, return True.
    # Otherwise, if the user's move is not in the proper range,
    # return False.
    # Otherwise, if the user's move is in the proper range and the tic tac
    # toe field has already been filled, return False.
    if (user_move in range(9)) and (game_board[user_move] == " "):
        return True
    elif user_move not in range(9):
        print("Invalid move! Try again.")
        return False
    elif (game_board[user_move] == "x") or (game_board[user_move] == "o"):
        print("Field already taken. Choose another field.")
        return False


def update_game_board_computer(computer_move):
    """
    Update the game board with the computer's move.

    Arguments:
        computer_move (int): the computer's move
    """

    # Keep getting a new move until the move is valid.
    while validate_computer_move(computer_move) == False:
        computer_move = get_computer_move()

    # Update the tic tac toe board with the computer's valid move.
    game_board[computer_move] = "x"


def update_game_board_user(user_move):
    """
    Update the game board with the user's move.

    Arguments:
        user_move (int): the user's move
    """

    # Keep prompting the user for a new move until the move is valid.
    while validate_user_move(user_move) == False:
        user_move = get_user_move()

    # Update the tic tac toe board with the user's valid move.
    game_board[user_move] = "o"


def get_game_status():
    """Return the status of the tic tac toe game at any time."""
    game_status = ""

    # If the computer has three x's in a row or other combination,
    # declare a computer victory.
    if (game_board[0] == game_board[1] == game_board[2] == "x"):
        game_status = "computer victory"
    elif (game_board[3] == game_board[4] == game_board[5] == "x"):
        game_status = "computer victory"
    elif (game_board[6] == game_board[7] == game_board[8] == "x"):
        game_status = "computer victory"
    elif (game_board[0] == game_board[3] == game_board[6] == "x"):
        game_status = "computer victory"
    elif (game_board[1] == game_board[4] == game_board[7] == "x"):
        game_status = "computer victory"
    elif (game_board[2] == game_board[5] == game_board[8] == "x"):
        game_status = "computer victory"
    elif (game_board[0] == game_board[4] == game_board[8] == "x"):
        game_status = "computer victory"
    elif (game_board[6] == game_board[4] == game_board[2] == "x"):
        game_status = "computer victory"

    # Otherwise, if the user has three o's in a row or other combination,
    # declare a user victory.
    elif (game_board[0] == game_board[1] == game_board[2] == "o"):
        game_status = "user victory"
    elif (game_board[3] == game_board[4] == game_board[5] == "o"):
        game_status = "user victory"
    elif (game_board[6] == game_board[7] == game_board[8] == "o"):
        game_status = "user victory"
    elif (game_board[0] == game_board[3] == game_board[6] == "o"):
        game_status = "user victory"
    elif (game_board[1] == game_board[4] == game_board[7] == "o"):
        game_status = "user victory"
    elif (game_board[2] == game_board[5] == game_board[8] == "o"):
        game_status = "user victory"
    elif (game_board[0] == game_board[4] == game_board[8] == "o"):
        game_status = "user victory"
    elif (game_board[6] == game_board[4] == game_board[2] == "o"):
        game_status = "user victory"

    # Otherwise, if no fields remain and neither the user or the computer
    # have three x's or o's in a row or other combination, declare a draw.
    elif (
        (" " not in game_board)
        and (game_status != "computer victory")
        and (game_status != "user victory")
    ):
        game_status = "no victory"

    return game_status


def main():
    INSTRUCTIONS = """
    |---------------------------------------------------------------------|
    |How To Play:                                                         |                                                                   |
    | - When the game starts, the tic tac toe board is displayed.         |
    | - The computer then makes a move.                                   |
    | - Once the computer has made its move, you may make your move.      |
    | - When that time comes along, choose a number from 1 to 9.          |
    | - This number corresponds to the fields on the tic tac toe board,   |
    |   which are numbered left to right, top to bottom.                  |
    | - To win, get three o's in a row on the tic tac toe board           |
    |                                                                     |  
    |Example:                                                             |                                                                |
    |If a player wanted to choose the field in the upper right-hand       |
    |corner of the tic tac toe board, they would choose the number 3.     |
    |                                                                     |
    |Good luck!                                                           |
    |---------------------------------------------------------------------|
    """
    CLOSING_MESSAGE = "Thanks for playing!"
    
    print("--------------------")
    print("Tic ... Tac ... Toe!")
    print("--------------------")
    print(f"\n{INSTRUCTIONS}")
    print("Game board:")
    display_game_board()
    sleep(2)
    
    # Initiate the main program loop.
    while True:
        computer_move = get_computer_move()
        update_game_board_computer(computer_move)
        print("Computer move:")
        display_game_board()
        sleep(2)

        game_status = get_game_status()

        if game_status == "computer victory":
            print("I win!")
            print(CLOSING_MESSAGE)
            break
        elif game_status == "user victory":
            print("You win!")
            print(CLOSING_MESSAGE)
            break
        elif game_status == "no victory":
            print("The game ended, but neither of us won.")
            print(CLOSING_MESSAGE)
            break

        user_move = get_user_move()
        update_game_board_user(user_move)
        print("User move:")
        display_game_board()
        sleep(2)

        game_status = get_game_status()

        if game_status == "computer victory":
            print("I win!")
            print(CLOSING_MESSAGE)
            break
        elif game_status == "user victory":
            print("You win!")
            print(CLOSING_MESSAGE)
            break
        elif game_status == "no victory":
            print("The game ended, but neither of us won.")
            print(CLOSING_MESSAGE)
            break


if __name__ == "__main__":
    main()
