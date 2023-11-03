import random
from questions import easy_questions
random.shuffle(easy_questions)

def main():
    """
    Main function with welcome screen and selection
    Starts the game after user inputs 'Play'
    """
    print("Welcome to Who Wants To Be A Millionaire")
    select_screen = input("Select:\n(Play|Rules)\n")
    if select_screen == "Play":
        player_name = input("Enter Your Name: ")
        print("Here..")
        print("We..")
        print("Go!")
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
    for question_data in easy_questions:  # Easy questions from questions.py stored into variables
        easy_question = question_data['question']
        easy_choices = question_data['choices']
        easy_answer = question_data['answer']
    
        print(easy_question) 
        for choice in easy_choices: 
            print(choice)
    
        player_answer = input("Choose an answer (A, B, C or D): ")

        if player_answer == easy_answer:  # Statement to check if user answer matches
            print("Correct")
        else:
            print(f"Wrong answer\nCorrect answer was: {easy_answer}")
        break

main()
print("Thank you for playing, better luck next time!")