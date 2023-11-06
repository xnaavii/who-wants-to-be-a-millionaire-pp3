import time
import random
import os
import platform
from game.google_sheet import append_highscore, show_highscore
from game.questions import easy_questions, normal_questions, hard_questions
from game.error_handling import (
    get_players_answer,
    get_player_name,
    play_again,
    play_rules,
    get_player_difficulty,
)
from game.prizes import prizes


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    """
    Main function with welcome screen and selection
    Starts the game after user inputs 'Play'
    """
    print("\nWelcome to Who Wants To Be A Millionaire")
    time.sleep(0.3)
    select_screen = play_rules()
    time.sleep(0.3)
    if select_screen == "play":
        print("\nHere..\n")
        time.sleep(0.3)
        print("We...\n")
        time.sleep(0.3)
        print("Go!\n")
        game_setup()  # Game starts
    elif select_screen == "rules":
        print("\nRules for 'Who Wants to Be a Millionaire?' Game\n")
        print(
            "Objective: The objective of the game is to answer a series of\nmultiple-choice questions correctly to accumulate as much money as possible.\n"
        )
        game_setup()
    elif select_screen == "highscore":
        show_highscore()


def game_setup():
    """
    Asks for user name and difficulty
    After the required input, game starts
    """
    player_name = get_player_name()
    # Get difficulty
    difficulty = get_player_difficulty()
    play_round(player_name, difficulty)


def play_round(player_name, difficulty="easy"):
    """
    Game logic for when the game starts
    Displays question with the set of choices
    On wrong response, player is provided with the correct answer
    """
    score = 0
    questions = []
    correct_answers = 0
    # Questions are extracted based on game difficulty
    if difficulty == "easy":
        questions = easy_questions
    elif difficulty == "normal":
        questions = normal_questions
    elif difficulty == "hard":
        questions = hard_questions

    random.shuffle(questions)
    for question_data in questions:  # Questions from questions.py stored into variables
        time.sleep(0.7)
        clear_terminal()
        question = question_data["question"]
        choices = question_data["choices"]
        answer = question_data["answer"]

        print(f"Player: {player_name}")
        print(f"Difficulty: {difficulty}")
        print(f"Current score: ${score}\n")
        time.sleep(0.5)
        print(f"{question}\n")
        time.sleep(0.5)
        for choice in choices:
            print(f"{choice}\n")
            time.sleep(0.5)

        player_answer = get_players_answer()

        if player_answer == answer:  # Statement to check if user answer matches
            print("...\n")
            time.sleep(0.3)
            print("....\n")
            time.sleep(0.3)
            score = prizes[correct_answers]
            correct_answers += 1  # Keep count of the correct answers
            time.sleep(0.3)
            print(
                f"Correct answer, {player_name}!\n"
            )  # Show player name and score during gameplay
            time.sleep(0.5)
            continue
        elif player_answer != answer:
            print("...\n")
            time.sleep(0.3)
            print("....\n")
            time.sleep(0.3)
            print(f"\nWrong answer\n\nCorrect answer was: {answer}\n")
        break

    if correct_answers == 10:  # Checks if all questions are answered
        score = 10000000
        print(f"Congratulations! You've won ${score}\n")
    elif correct_answers >= 1:
        print(
            f"{player_name}, you've secured at least ${prizes[correct_answers -1]}.\n"
        )
    else:
        print("Sorry, you didn't win anything.\n")
    append_highscore(player_name, difficulty, score)

    again = play_again(player_name)  # Validate user input on play again
    if again == "yes":
        print("\nHere..\n")
        time.sleep(0.3)
        print("We...\n")
        time.sleep(0.3)
        print("Go!\n")
        play_round(player_name)
    elif again == "no":
        clear_terminal()
        # Quit the game after user input
        quit_game()

def quit_game():
    # Function to quit the game
    print("Thank you for playing!\n")
    quit()
