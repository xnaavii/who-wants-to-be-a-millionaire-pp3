import time
import random
from questions import easy_questions
from error_handling import get_players_answer

def main():
    """
    Main function with welcome screen and selection
    Starts the game after user inputs 'Play'
    """
    print("\nWelcome to Who Wants To Be A Millionaire")
    time.sleep(0.5)
    print("\nSelect")
    select_screen = input("\n[Play]|[Rules]: ")
    time.sleep(0.5)
    if select_screen == "Play":
        print("\nHere..\n")
        time.sleep(0.5)
        print("We...\n")
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
    random.shuffle(easy_questions)
    player_name = input("Enter Your Name: ")
    score = 0
    for question_data in easy_questions:  # Easy questions from questions.py stored into variables
        easy_question = question_data['question']
        easy_choices = question_data['choices']
        easy_answer = question_data['answer']

        time.sleep(1)
        print(f"\n{easy_question}\n") 
        time.sleep(1)
        for choice in easy_choices: 
            print(f"{choice}\n")
            time.sleep(1)
        
        player_answer = get_players_answer()
        
        if player_answer == easy_answer:  # Statement to check if user answer matches
            print("...\n")
            time.sleep(1)
            print("....\n")
            time.sleep(1)
            score += 100
            time.sleep(0.5)
            print(f"\nCorrect answer, {player_name}! Your score is {score}$\n") # Show player name and score during gameplay
            time.sleep(0.5)
            continue
        else:
            print("...\n")
            time.sleep(1)
            print("....\n")
            time.sleep(1)
            print(f"\nWrong answer\n\nCorrect answer was: {easy_answer}\n")
        break
    print("Thank you for playing, better luck next time!\n")
    print(f"Your score was: {score}$\n")
    play_again = input("Play again? [Yes][No]")
    
    if play_again == "Yes":
        print("\nHere..\n")
        time.sleep(0.5)
        print("We...\n")
        time.sleep(0.5)
        print("Go!\n")
        play_round()


main()
