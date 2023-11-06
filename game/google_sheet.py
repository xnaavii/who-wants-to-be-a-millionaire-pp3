import gspread
from google.oauth2.service_account import Credentials

# Set up google sheet credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access the sheet
SHEET = GSPREAD_CLIENT.open("highscore_pp3") 
highscore_sheet = SHEET.worksheet("highscore")

def append_highscore(player_name, difficulty, score):
    # Function to record the score inside google sheet file
    highscore_data = [player_name, difficulty, score]
    highscore_sheet.append_rows([highscore_data])

