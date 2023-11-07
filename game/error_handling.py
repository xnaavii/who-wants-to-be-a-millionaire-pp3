from colorama import Style, Fore, Back, init
init()

def get_players_answer():
    """
    Handles the error on user input
    Returns the correct input to continue playing
    """
    valid_input = ["A", "B", "C", "D"]  # Inputs that are requested to continue
    while True:
        try:
            player_answer = input(Style.DIM + "Choose an answer (A, B, C or D): " + Style.RESET_ALL).upper()
            if player_answer in valid_input:
                return player_answer
            else:
                print(Fore.RED + "Invalid choice. " + Style.RESET_ALL + "Please enter A, B, C, or D.\n")
        except Exception as e:
            print(f"An error occurred: {e}")


def play_rules():
    """
    Handles the error on play_rules input
    """
    valid_response = ["play", "rules", "highscore"]
    while True:
        try:
            print("\nPlease select ", end="")
            select_screen = input(Fore.MAGENTA + "[Play][Rules][Highscore]: " + Style.RESET_ALL).lower()
            if select_screen in valid_response:
                return select_screen
            else:
                print(Fore.RED + "Invalid selection." + Style.RESET_ALL) 
        except Exception as e:
            print(f"An error occured: {e}")


def get_player_name():
    name = input("Enter your name: ")
    return name


def get_player_difficulty():
    """
    Validate the user input on difficulty instance
    """
    valid_difficulty = ["easy", "normal", "hard"]
    while True:
        print("\nChoose difficulty ", end="")
        difficulty = input(Fore.MAGENTA + "[Easy][Normal][Hard]: " + Style.RESET_ALL).lower()
        if difficulty in valid_difficulty:
            return difficulty
        else:
            print(Fore.RED + "Invalid selection." + Style.RESET_ALL)


def play_again(player_name):
    # Error handling for play again instance
    play_again_response = ["yes", "no"]
    while True:
        try:
            print(Style.BRIGHT + f"{player_name}, ", end="")
            play_again = input("Would you like to play again? [Yes][No]: " + Style.RESET_ALL).lower()
            if play_again in play_again_response:
                return play_again
            else:
                print("Invalid selection. Please select [Yes] or [No]: ")
        except Exception as e:
            print(f"An error occured: {e}")
