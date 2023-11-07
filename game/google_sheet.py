import gspread
from google.oauth2.service_account import Credentials

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
highscore_sheets = {
    "easy": SHEET.worksheet("easy"),
    "normal": SHEET.worksheet("normal"),
    "hard": SHEET.worksheet("hard")
}


def append_highscore(player_name, difficulty, score):
    # Function to record the score inside google sheet file
    highscore_data = [player_name, difficulty, score]
    
    highscore_sheet = highscore_sheets[difficulty]
    
    highscore_sheet.append_rows([highscore_data])


def show_highscore():
    # List of difficulty levels
    difficulties = ["easy", "normal", "hard"]
    
    for difficulty in difficulties:
        
        highscore_sheet = highscore_sheets[difficulty]  # Get the correct worksheet
        
        show_score = highscore_sheet.get_all_values()
        # Filter out rows with invalid data
        valid_scores = [row for row in show_score if len(row) == 3 and row[0] and row[2].isdigit()]
        
        if valid_scores:
            # Sort the score in desceding order
            valid_scores.sort(key=lambda x: int(x[2]), reverse=True)
        
            print(f"Top 5 High Scores for {difficulty} Difficulty:")
            for rank, item in enumerate(valid_scores[:5], start=1):
                player_name, _, score = item
                print(f"{rank}. Name: {player_name}, Score: {score}")
            print()

