Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def game_board():
    """
    
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
    name = name.capitalize()

    check_user_name(name)


def check_user_name(name):
    """
    Validate users name by checking that they've inserted only letters
    or they're sent back to input their names again with an error message
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
    Asks player if they want to be "X" or "O" and
    Computer becomes the other one
    """
    print("")
    user_player = input("Would you like to be X or O?\n")
    computer_player = "" 

    user_player = user_player.upper()
  
    if user_player == "X":
        print("You are X and the Computer is O!")
        computer_player = "O" 
        play_game()
    elif user_player == "O":
        print("You are O and the Computer is X!")
        computer_player = "X" 
        play_game()
    else:
        print("")
        print("Invalid data: Please insert X or O.")
        players()
    
    return user_player, computer_player


def check_board():
    """
    
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows
        if Board[i * 3] == Board[i * 3 + 1] == Board[i * 3 + 2] != " ":
            return Board[i * 3]
  
        # Check columns
        if Board[i] == Board[i + 3] == Board[i + 6] != " ":
            return Board[i]
  
    # Check diagonals
    if Board[0] == Board[4] == Board[8] != " ":
        return Board[0]
    if Board[2] == Board[4] == Board[6] != " ":
        return Board[2]
    
    # If no 
    return None


def check_turn():
    """
    
    """
    return "X" if turn % 2 == 0 else "O"


def play_game(user_player, computer_player, turn):
    """
    
    """
    global Board
    
    print("")
    print(f"You are {user_player} and the Computer is {computer_player}.")
    print("Rules: The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")

    turn = 0
    
    while True:
        game_board()
        choice = input("Please select a number from 1 to 9:\n")
    
        if Board[int(choice) - 1] not in ["X", "O"]:
            turn += 1
            Board[int(choice) - 1] = check_turn(turn)
            winner = check_board(Board)
    
            if winner:
                print(f"{winner} is the winner!")
                break
    
            if turn == 9:
                print("It's a tie!")
                break
        else:
            print("Invalid move. That cell is already taken. Please choose again.")


def play_again():
    """
    
    """
    play_again = input("Would you like to play again? (Y/N)\n")

    play_again = play_again.upper()
    if play_again == "Y":
        start_game()
    else:
        print("Thank you for playing!")


def main():
    """
    Call on game functions
    """
    start_game()
    play_again()

main()