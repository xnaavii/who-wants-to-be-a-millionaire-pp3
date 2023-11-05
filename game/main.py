import time
import random
from game.questions import easy_questions
from game.error_handling import get_players_answer, get_player_name, play_again, play_rules

def main():
    """
    Main function with welcome screen and selection
    Starts the game after user inputs 'Play'
    """
    print("\nWelcome to Who Wants To Be A Millionaire")
    time.sleep(0.5)
    print("\nSelect")
    select_screen = play_rules()
    time.sleep(0.5)
    if select_screen == "Play":
        print("\nHere..\n")
        time.sleep(0.5)
        print("We...\n")
        time.sleep(0.5)
        print("Go!\n")
        game_setup() # Game starts 
    elif select_screen == "Rules":
        print("Rules for 'Who Wants to Be a Millionaire?' Game:")
        print("Objective: The objective of the game is to answer a series of multiple-choice questions correctly to accumulate as much money as possible.\n")

def game_setup():
    player_name = get_player_name()
    # Get difficulty
    # difficulty = get_player_difficulty()
    play_round(player_name)

def play_round(player_name, difficulty="easy"):
    """
    Game logic for when the game starts
    Displays question with the set of choices
    On wrong response, player is provided with the correct answer
    """
    if difficulty == "easy":
        questions = easy_questions
    random.shuffle(questions)
    score = 0
    for question_data in questions:  # Easy questions from questions.py stored into variables
        question = question_data['question']
        choices = question_data['choices']
        answer = question_data['answer']

        time.sleep(1)
        print(f"\n{question}\n") 
        time.sleep(1)
        for choice in choices: 
            print(f"{choice}\n")
            time.sleep(1)
        
        player_answer = get_players_answer()
        
        if player_answer == answer:  # Statement to check if user answer matches
            print("...\n")
            time.sleep(0.5)
            print("....\n")
            time.sleep(0.5)
            score += 100
            time.sleep(0.5)
            print(f"\nCorrect answer, {player_name}! Your score is {score}$\n") # Show player name and score during gameplay
            time.sleep(0.5)
            continue
        else:
            print("...\n")
            time.sleep(0.5)
            print("....\n")
            time.sleep(0.5)
            print(f"\nWrong answer\n\nCorrect answer was: {answer}\n")
        break
    print("Thank you for playing, better luck next time!\n")
    print(f"Your score was: {score}$\n")
    again = play_again(player_name)
    if again == "Yes":
        print("\nHere..\n")
        time.sleep(0.5)
        print("We...\n")
        time.sleep(0.5)
        print("Go!\n")
        play_round(player_name)
