def get_players_answer():
    """
    Handles the error on user input
    Returns the correct input to continue playing
    """
    valid_input = ["A", "B", "C", "D"] # Inputs that are requested to continue
    while True:
        try:
            player_answer = input("Choose an answer (A, B, C or D): ")
            if player_answer in valid_input:
                return player_answer
            else:
                print("Invalid choice. Please enter A, B, C, or D.\n")
        except Exception as e:
            print(f"An error occurred: {e}")