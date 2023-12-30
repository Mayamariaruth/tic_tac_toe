def game_board(board):
    """
    
    """
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def start_game():
    """
    Prints a welcome message and asks for users name with an input.
    Calls for check_user_name function to validate users input.
    """
    game_board(board)
    print("")
    print("Welcome to Tic Tac Toe!")
    print("We first need to know who is challenging our fierce Computer.")
    name = input("Please enter your name:\n")
    check_user_name(name)

def check_user_name(name):
    """
    Validate users name by checking that they've inserted only letters
    or they're sent back to input their names again with an error message
    """
    if name.isalpha():
        print(f"Thank you {name}!")
    else:
        print("")
        print("Invalid data: Please insert your name with only letters.")
        start_game()   

def players():
    """
    Asks player if they want to be "X" or "O" and
    Computer becomes the other one
    """
    print("")
    user_player = input("Would you like to be X or O?\n")
    computer_player = "" 

    user_player = user_player.upper()
  
    if user_player == "X":
        print("You are X and the Computer is O!")
        computer_player = "0" 
    elif user_player == "O":
        print("You are O and the Computer is X!")
        computer_player = "X" 
    else:
        print("")
        print("Invalid data: Please insert X or O.")
        players()
    
    return user_player, computer_player
  


def play_game():
    """
    
    """

def player_positions():
    """
    
    """

def check_winner():
    """
    
    Asks user if they want to play again and is taken to another round with
    the play_game function
    """


def main():
    """
    Call on all game functions, all collected inside one function for
    cleaner code
    """
    start_game()

main()