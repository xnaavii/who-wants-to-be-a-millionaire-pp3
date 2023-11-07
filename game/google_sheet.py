import gspread
import colorama
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style, init

init()
# Set up google sheet credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access the sheet
SHEET = GSPREAD_CLIENT.open("highscore_pp3")
# Define a dictionary to store references to different worksheets
highscore_sheets = {
    "easy": SHEET.worksheet("easy"),
    "normal": SHEET.worksheet("normal"),
    "hard": SHEET.worksheet("hard")
}


def append_highscore(player_name, difficulty, score):
    # Function to record the score inside google sheet file
    highscore_data = [player_name, difficulty, score]
    # Access the correct worksheet for the given difficulty
    highscore_sheet = highscore_sheets[difficulty]
    # Append the highscore data to the worksheet
    highscore_sheet.append_rows([highscore_data])


def show_highscore():
    """
    Function to show user highscore on game startup selection
    Shows Top 5 high scores in each difficulty 
    Replaces the list with the new highscore (if achieved)
    """
    # List of difficulty levels
    difficulties = ["easy", "normal", "hard"]
    
    for difficulty in difficulties:
        # Get the correct worksheet for the current difficulty
        highscore_sheet = highscore_sheets[difficulty]  
        
        show_score = highscore_sheet.get_all_values()
        
        # Filter out rows with invalid data
        valid_scores = []
        for row in show_score:
            if len(row) == 3 and row[0] and row[2].isdigit():
                valid_scores.append(row)
        
        if valid_scores:
            # Sort the score in desceding order
            valid_scores.sort(key=lambda x: int(x[2]), reverse=True)

            # Display the top 5 high scores for the current difficulty
            print(Fore.YELLOW + f"\nTop 5 High Scores for {difficulty.capitalize()} Difficulty:" + Style.RESET_ALL)
            for rank, item in enumerate(valid_scores[:5], start=1):
                player_name, _, score = item
                print(f"{rank}. Name: {player_name}, Score: {score}")
            
            if len(valid_scores) > 5:
                # Find the lowest score among the top 5 scores
                lowest_top_score = min(int(row[2]) for row in valid_scores[:5])

                # Get the new score
                new_score = int(valid_scores[5][2])
                if new_score > lowest_top_score:
                    # Find the index of the lowest score
                    for i, row in enumerate(valid_scores):
                        if int(row[2]) == lowest_top_score:
                            lowest_top_score = i
                            break
                    
                    # Calculate the row number to remove
                    row_to_remove = show_score.index(valid_scores[lowest_top_score]) + 2
                    # Delete the lowest score
                    highscore_sheet.delete_rows(row_to_remove)
                    # Append the updated top 5 scores
                    highscore_sheet.append_table(valid_scores[:5])
            print()

