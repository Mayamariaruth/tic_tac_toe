import random

# Global variable used in most functions
Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def game_board():
    """
    Prints the game board design with each number/box iteration.
    """
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print("---------")
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print("---------")
    print(Board[6] + " | " + Board[7] + " | " + Board[8])


def start_game():
    """
    Prints a welcome message and asks for users name with an input.
    Calls for check_user_name function to validate users input.
    """
    game_board()
    print("")
    print("Welcome to Tic Tac Toe!")
    print("We first need to know who is challenging our fierce Computer.")
    name = input("Please enter your name:\n").capitalize()

    check_user_name(name)


def check_user_name(name):
    """
    Validate users name by checking that they've inserted only letters
    or they're sent back to input their names again with an error message.
    """
    if name.isalpha():
        print(f"Welcome {name}!")
        players()
    else:
        print("")
        print("Invalid data: Please insert your name with only letters.")
        start_game()


def players():
    """
    Asks user if they want to be "X" or "O" and
    Computer becomes the other one or if user inputs
    anything other than "X, O", they receive an error message
    and are asked again.
    """
    print("")
    user_player = input("Would you like to be X or O?\n").upper()
    computer_player = ""

    if user_player == "X":
        print("You are X and the Computer is O!")
        computer_player = "O"
        play_game(user_player, computer_player, Board)
    elif user_player == "O":
        print("You are O and the Computer is X!")
        computer_player = "X"
        play_game(user_player, computer_player, Board)
    else:
        print("")
        print("Invalid data: Please insert X or O.")
        players()

    return user_player, computer_player


def check_winner(Board):
    """
    Defines the winning combinations as lists
    and check's the board for the winner
    by looking at the combinations for three matching symbols
    (and not empty spaces) and then returns the symbol as the winner
    """
    # Define winning combinations as lists
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
        [0, 4, 8], [2, 4, 6]   # Diagonals
    ]

    # Checks for three matching symbols with the combinations
    for combo in winning_combinations:
        if all(Board[i] == Board[combo[0]] and Board[i] != " " for i in combo):
            return Board[combo[0]]


def play_game(user_player, computer_player, Board):
    """
    Alternates between users/computers turn and receives an
    input from the user that is validated
    (spot is empty and input is a number or they receive an error).
    The selected number changes to users or computers symbol.
    """
    turn = 0

    while True:
        print("")
        game_board()
        print("")
        print(f"You are {user_player} and the Computer is {computer_player}.")
        print("Rules: The first player to get 3 of their marks in a row")
        print("(vertically, horizontally, or diagonally) is the winner.")

        # User's turn
        if turn % 2 == 0:
            choice = input("Please select a number from 1 to 9:\n")
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    if Board[int(choice) - 1] not in ["X", "O"]:
                        turn += 1
                        Board[choice - 1] = user_player
                        winner = check_winner(Board)

                        if winner:
                            print("")
                            game_board()
                            print("")
                            print(f"{winner} is the winner!")
                            break

                        if turn == 9:
                            print("")
                            game_board()
                            print("")
                            print("It's a tie!")
                            break
                    else:
                        print("That cell is taken. Please choose again.")
                        ConnectionRefusedError
                        continue
                else:
                    print("Invalid. Please choose a number from 1 to 9.")
                    ConnectionRefusedError
                    continue
            except ValueError:
                print("Invalid input. Please choose a number from 1 to 9.")
                continue

        # Computer's turn
        computer_move(computer_player, Board)
        turn += 1
        winner = check_winner(Board)

        if winner:
            print("")
            game_board()
            print("")
            print(f"{winner} is the winner!")
            break

        if turn == 9:
            print("")
            game_board()
            print("")
            print("It's a tie!")
            break


def computer_move(computer_player, Board):
    """
    Acts as the Computer and generates a random number
    between 9 as its mark selection
    (that is not already marked with "X" or "O")
    """
    # List of empty positions on the board
    empty_positions = [i for i in range(9) if Board[i] not in ["X", "O"]]

    # If there are empty positions, the computer chooses a random one
    if empty_positions:
        computer_choice = random.choice(empty_positions)
        Board[computer_choice] = computer_player


def play_again():
    """
    Asks user if they want to play again and initiates
    start_game function or prints a thank you message.
    """
    while True:
        play_again = input("Would you like to play again? (Y/N)\n").upper()
        if play_again == "Y":
            start_game()
            break
        elif play_again == "N":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter Y/N.")


def main():
    """
    Call on game functions
    """
    start_game()
    play_again()


main()