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
    """
    game_board(board)
    print("")
    print("Welcome to Tic Tac Toe!")
    print("We first need to know who is challenging our fierce Computer.")
    name = input("Please enter your name:\n")
    check_user_name(name)

def check_user_name(name):
    """
    Validates users name by checking that they've inserted only letters
    or they're sent back to input their names again with an error message
    """
    if name.isalpha():
        print("Thank you!")
    else:
        print("Invalid data: Please insert your name with only letters.")
        start_game()   

def players():
    """
    Asks player if they want to be "X" or "O" and
    Computer becomes the other one


    """


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