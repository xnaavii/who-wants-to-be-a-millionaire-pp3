def get_players_answer():
    """
    Handles the error on user input
    Returns the correct input to continue playing
    """
    valid_input = ["A", "B", "C", "D"]  # Inputs that are requested to continue
    while True:
        try:
            player_answer = input("Choose an answer (A, B, C or D): ").upper()
            if player_answer in valid_input:
                return player_answer
            else:
                print("Invalid choice. Please enter A, B, C, or D.\n")
        except Exception as e:
            print(f"An error occurred: {e}")


def play_rules():
    """
    Handles the error on play_rules input
    """
    valid_response = ["play", "rules", "highscore"]
    while True:
        try:
            select_screen = input("\nPlease select [Play][Rules][Highscore]: ").lower()
            if select_screen in valid_response:
                return select_screen
            else:
                print(
                    "Invalid selection. Please select [Play],[Rules] or [Highscore]: "
                )
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
        difficulty = input("\nChoose difficulty [Easy][Normal][Hard]: ").lower()
        if difficulty in valid_difficulty:
            return difficulty
        else:
            print("Invalid selection. Please select [Easy],[Medium] or [Hard]")


def play_again(player_name):
    # Error handling for play again instance
    play_again_response = ["yes", "no"]
    while True:
        try:
            play_again = input(
                f"{player_name}, Would you like to play again? [Yes][No]: "
            ).lower()
            if play_again in play_again_response:
                return play_again
            else:
                print("Invalid selection. Please select [Yes] or [No]: ")
        except Exception as e:
            print(f"An error occured: {e}")
