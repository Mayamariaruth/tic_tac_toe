import os
import random

# Global variable used in most functions
board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]


# Code credit in docstring due to long url
def clear_console():
    """
    Clear the console.
    Code taken directly from url:
    https://www.delftstack.com/howto/python/python-clear-console/
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


# To clear the Heroku console before game start
clear_console()


def game_board():
    """
    Prints the game board design with each number/box iteration.
    """
    print("    " + board[0] + " | " + board[1] + " | " + board[2])
    print("    " + "---------")
    print("    " + board[3] + " | " + board[4] + " | " + board[5])
    print("    " + "---------")
    print("    " + board[6] + " | " + board[7] + " | " + board[8])


def start_game():
    """
    Prints a welcome message with title art
    and asks the player to enter "S" to start the game.
    """
    print("")
    print("""
    ████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
    ╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
    ░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
    ░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
    ░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
    ░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝
        """)
    print("")
    print("    Welcome to the fun game of Tic Tac Toe!")
    start = input("    Please enter S to start the game:\n    ").upper()

    if start == "S":
        user_name()
    else:
        clear_console()
        print("    Please enter S to start the game.")
        start_game()


def user_name():
    """
    Asks for user's name and validates it
    by checking that they've inserted only letters.
    """
    print("")
    print("    We first need to know who is challenging our fierce Computer.")
    name = input("    Please enter your name:\n    ").capitalize()

    if name.isalpha():
        print("")
        print(f"    Welcome {name}!")
        players()
    else:
        print("")
        print("    Invalid data: Please insert your name with only letters.")
        user_name()


def players():
    """
    Asks user if they want to be "X" or "O" and
    Computer becomes the other one.
    Validates user's input if they've entered anything other than "X, O".
    """
    user_player = input("    Would you like to be X or O?\n    ").upper()
    computer_player = ""

    if user_player == "X":
        computer_player = "O"
        play_game(user_player, computer_player, board)
    elif user_player == "O":
        computer_player = "X"
        play_game(user_player, computer_player, board)
    else:
        print("")
        print("    Invalid data: Please insert X or O.")
        players()

    return user_player, computer_player


def check_winner(board):
    """
    Defines the winning combinations as lists
    and checks the board for the winner
    by looking at the combinations for three matching symbols
    (and not empty spaces) and then returns the symbol as the winner
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
        [0, 4, 8], [2, 4, 6]   # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == board[combo[0]] and board[i] != " " for i in combo):
            return board[combo[0]]


def play_game(user_player, computer_player, board):
    """
    Alternates between users/computers turn
    but always starting with "X" and receives an
    input from the user that is validated
    (spot is empty and input is a number between 1-9).
    The selected number changes to user's or computer's symbol.
    """
    clear_console()
    turn = 0

    while True:
        print("")
        game_board()
        print("")
        print(
            f"    You are {user_player} and the Computer is {computer_player}."
        )
        print("")
        print("    Rules: The first player to get 3 of their marks in a row")
        print("    (vertically, horizontally, or diagonally) is the winner.")

        # User's turn
        if turn % 2 == (user_player == "O") and user_player in {"X", "O"}:
            print("")
            choice = input("    Please select a number from 1 to 9:\n    ")
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    if board[choice - 1] not in ["X", "O"]:
                        turn += 1
                        board[choice - 1] = user_player
                        winner = check_winner(board)

                        if winner:
                            clear_console()
                            print("")
                            game_board()
                            print("")
                            print(f"    {winner} is the winner!")
                            play_again()
                            break

                        if turn == 9:
                            clear_console()
                            print("")
                            game_board()
                            print("")
                            print("    It's a tie!")
                            play_again()
                            break
                    else:
                        print("    That cell is taken. Please choose again.")
                        ConnectionRefusedError
                        continue
                else:
                    print(
                        "    Invalid. Please choose a number from 1 to 9."
                    )
                    ConnectionRefusedError
                    continue
            except ValueError:
                print("    Invalid. Please choose a number from 1 to 9.")
                continue

        clear_console()

        # Computer's turn
        computer_move(computer_player, board)
        turn += 1
        winner = check_winner(board)

        if winner:
            clear_console()
            print("")
            game_board()
            print("")
            print(f"    {winner} is the winner!")
            play_again()
            break

        if turn == 9:
            clear_console()
            print("")
            game_board()
            print("")
            print("    It's a tie!")
            play_again()
            break


def computer_move(computer_player, board):
    """
    Acts as the Computer and generates a random number
    between 9 as its mark selection
    (that is not already marked with "X" or "O")
    """
    empty_positions = [i for i in range(9) if board[i] not in ["X", "O"]]

    if empty_positions:
        computer_choice = random.choice(empty_positions)
        board[computer_choice] = computer_player


def play_again():
    """
    Asks user if they want to play again and initiates
    start_game function and prints a thank you message if user selected "N".
    Resets game board by defining the global variable with its intitial value.
    """
    global board
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        print("")
        play_again = input("    Would you like to play again?(Y/N)\n    ")
        play_again = play_again.upper()

        if play_again == "Y":
            clear_console()
            start_game()
            break
        elif play_again == "N":
            clear_console()
            print("    Thank you for playing!")
            start_game()
            break
        else:
            print("    Invalid input. Please enter Y/N.")


start_game()
