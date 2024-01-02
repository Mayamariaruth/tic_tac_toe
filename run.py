import random

# Global variables to be able to use in most functions
Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
Turn = 0

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
    name = input("Please enter your name:\n")

    # Make user name capitalized
    name = name.capitalize()

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
    Computer becomes the other one or if user inputs anything other than "X, O",
    they receive an error message and are asked again.
    """
    print("")
    user_player = input("Would you like to be X or O?\n")
    computer_player = "" 

    # Make user's input uppercase in case they write "X" or "O" in small letters
    user_player = user_player.upper()
  
    if user_player == "X":
        print("You are X and the Computer is O!")
        computer_player = "O" 
        play_game(user_player, computer_player, Board, Turn)
    elif user_player == "O":
        print("You are O and the Computer is X!")
        computer_player = "X" 
        play_game(user_player, computer_player, Board, Turn)
    else:
        print("")
        print("Invalid data: Please insert X or O.")
        players()
    
    return user_player, computer_player


def check_winner(Board):
    """
    Defines the winning combinations as lists and check's the board for the winner 
    by looking at winning combination for three matching symbols (and not empty space)
    and then returns the symbol (as the winner in the play_game function)
    """
    # Define winning combinations as lists
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6] # Diagonals
    ]

    # Checks if there is a symbol on every index in each winning combination list
    for combo in winning_combinations:
        if all(Board[i] == Board[combo[0]] and Board[i] != " " for i in combo):
            return Board[combo[0]]


def check_turn(Turn):
    """
    Alternates between turns for players with an odd or even number ("O" is even and "X" is odd)
    """
    return "O" if Turn % 2 == 0 else "X"


def computer_move(computer_player, Board):
    """
    Acts as the Computer and generates a random number between 9 as its mark selection
    (that is not already marked with "X" or "O")
    """
    # List of empty positions on the board
    empty_positions = [i for i in range(9) if Board[i] not in ["X", "O"]]

    # If there are empty positions, the computer chooses a random one
    if empty_positions:
        computer_choice = random.randint(empty_positions)
        Board[computer_choice] = computer_player
    else:
        print("The board is full. It's a tie!")


def play_game(user_player, computer_player, Board, Turn):
    """
    
    """
    while True:
        print("")
        game_board()
        print("")
        print(f"You are {user_player} and the Computer is {computer_player}.")
        print("Rules: The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")

        # User's turn
        choice = input("Please select a number from 1 to 9:\n")
        try:
            choice = int(choice)
            if Board[int(choice) - 1] not in ["X", "O"]:
                Turn += 1
                Board[choice - 1] = check_turn(Turn)
                winner = check_winner(Board)
        
                if winner:
                    print(f"{winner} is the winner!")
                    break
        
                if Turn == 9:
                    print("It's a tie!")
                    break
            else:
                print("Invalid move. That cell is already taken. Please choose again.")
        except ValueError:
            print("Invalid input. Please choose a number from 1 to 9.")

        # Computer's turn
        computer_move(computer_player, Board)

def play_again():
    """
    
    """
    play_again = input("Would you like to play again? (Y/N)\n")

    play_again = play_again.upper()
    try:
        if play_again == "Y":
            start_game()
        else:
            print("Thank you for playing!")
    except ValueError:
        print("Invalid input. Please choose Y/N.")


def main():
    """
    Call on game functions
    """
    start_game()
    play_again()

main()