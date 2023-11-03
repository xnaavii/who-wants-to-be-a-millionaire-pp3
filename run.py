import time
import random
from questions import easy_questions
from error_handling import get_players_answer
random.shuffle(easy_questions)

def main():
    """
    Main function with welcome screen and selection
    Starts the game after user inputs 'Play'
    """
    print("Welcome to Who Wants To Be A Millionaire")
    time.sleep(0.5)
    select_screen = input("Select:\n(Play|Rules)\n")
    time.sleep(0.5)
    if select_screen == "Play":
        player_name = input("Enter Your Name: ")
        print("Here..")
        time.sleep(0.5)
        print("We...")
        time.sleep(0.5)
        print("Go!\n")
        play_round()  # Game starts 
    elif select_screen == "Rules":
        print("Rules for 'Who Wants to Be a Millionaire?' Game:")
        print("Objective: The objective of the game is to answer a series of multiple-choice questions correctly to accumulate as much money as possible.\n")

def play_round():
    """
    Game logic for when the game starts
    Displays question with the set of choices
    On wrong response, player is provided with the correct answer
    """
    
    score = 0
    for question_data in easy_questions:  # Easy questions from questions.py stored into variables
        easy_question = question_data['question']
        easy_choices = question_data['choices']
        easy_answer = question_data['answer']
    
        print(f"{easy_question}\n") 
        time.sleep(1)
        for choice in easy_choices: 
            print(f"{choice}\n")
            time.sleep(1.2)
        
        player_answer = get_players_answer()
        
        if player_answer == easy_answer:  # Statement to check if user answer matches
            print("...\n")
            time.sleep(1)
            print("....\n")
            time.sleep(2)
            print("Correct\n")
            score += 100
            time.sleep(0.5)
            continue 
        else:
            print(f"Wrong answer\nCorrect answer was: {easy_answer}")
            
        break

    print("Thank you for playing, better luck next time!\n")
    print(f"Your score was: {score}$")

main()
