def get_players_answer():
    """
    Handles the error on user input
    Returns the correct input to continue playing
    """
    valid_input = ["A", "B", "C", "D"] # Inputs that are requested to continue
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
    valid_response = ["Play", "Rules"]
    while True:
        try:
            select_screen = input("Please select [Play][Rules]: ").capitalize()
            if select_screen in valid_response:
                return select_screen
            else:
                print("Invalid selection. Please select [Play] or [Rules]: ")
        except Exception as e:
            print(f"An error occured: {e}")

def get_player_name():
    name = input("Enter your name: ")
    return name

def play_again(player_name):
    # Error handling for play again instance
    play_again_response = ["Yes", "No"]
    while True:
        try:
            play_again = input(f"{player_name} Would you like to play again? [Yes][No]: ").capitalize()
            if play_again in play_again_response:
                return play_again
            else:
                print("Invalid selection. Please select [Yes] or [No]: ")
        except Exception as e:
            print(f"An error occured: {e}")