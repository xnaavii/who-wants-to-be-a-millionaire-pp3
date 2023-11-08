import time
import random
import os
import platform
from colorama import Fore, Back, Style, init
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

init()


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
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "\nWelcome to Who Wants To Be A Millionaire\n"
        + Style.RESET_ALL
    )
    print(
        """
    ░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░▒▒▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░▒▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓░░░░░░░▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░░
    ░░░░░░░░░░░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒░░▓▓▓▓▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒░░░░░░░░░░
    ░░░░░░░░░░░░▒▓▓▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▒░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░
    ░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▓▓▓▓▒░░▒▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░
    ░░░░░░░░░░░▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒░░▒▒▒▒░░▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓░░░░░░░░░░
    ░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓▒░░░░▒▒▓▓▓▓▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▓▓▒▓▒▒░░░░░░░░░
    ░░░░░░░░░░░░░░░▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒░░░░░░░░░
    ░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒░░░░░░░░
    ░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▓▒▒▓▒▓▓▒░░░░░░░░
    ░░░░░░░░░░░░░░░▒▓▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒░░░░░░░
    ░░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▓▓▓▓▓▒▒▒▒▒▓▓▓▓▓▒▓▓▓▓▓░░▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▒▒░░░░░░░
    ░░░░░░░░░░░░░░░░▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▓▓▓▒░░░░░░░▒▓▓▓▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░
    ░░░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░▒▓▓▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░▒▒▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        """
        )
    time.sleep(0.3)
    select_screen = play_rules()
    time.sleep(0.3)
    if select_screen == "play":
        print(Style.DIM + "\nHere..\n")
        time.sleep(0.3)
        print("We...\n")
        time.sleep(0.3)
        print("Go!\n" + Style.RESET_ALL)
        game_setup()  # Game starts
    elif select_screen == "rules":
        clear_terminal()
        print(
            Fore.GREEN
            + "\nRules for 'Who Wants to Be a Millionaire?' Game\n"
            + Style.RESET_ALL
        )
        print(
            Fore.RED +
            "Objective: \n"
            + Style.RESET_ALL +
            "The objective of ", end=""
        )
        print("the game is to answer a series of ", end="")
        print("multiple-choice questions ", end="")
        print("correctly to accumulate as much money as possible.\n")
    elif select_screen == "highscore":
        show_highscore()
    game_setup()


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
    # Questions from questions.py stored into variables
    for question_data in questions:
        time.sleep(0.7)
        clear_terminal()
        question = question_data["question"]
        choices = question_data["choices"]
        answer = question_data["answer"]

        print(
            Fore.LIGHTBLUE_EX
            + "🕹️ Player: "
            + Style.RESET_ALL
            + f"{player_name}")
        print(
            Fore.LIGHTBLUE_EX
            + "Difficulty: "
            + Style.RESET_ALL +
            f"{difficulty.capitalize()}"
        )
        print(
            Fore.LIGHTBLUE_EX
            + "Current score: "
            + Fore.GREEN +
            f"${score}\n"
            + Style.RESET_ALL)
        time.sleep(0.5)
        # Print the questions out
        print(Fore.LIGHTWHITE_EX + f"{question}\n" + Style.RESET_ALL)
        time.sleep(0.5)
        # Print the choices available
        for choice in choices:
            print(f"{choice}\n")
            time.sleep(0.5)

        player_answer = get_players_answer()

        # Statement to check if user answer matches
        if player_answer == answer:
            print(Style.DIM + "...\n")
            time.sleep(0.3)
            print("....\n" + Style.RESET_ALL)
            time.sleep(0.3)
            score = prizes[correct_answers]
            # Keep count of the correct answers
            correct_answers += 1
            time.sleep(0.3)
            # Show player name and score during gameplay
            print(
                Style.BRIGHT
                + f"Correct answer, {player_name}!\n"
                + Style.RESET_ALL)
            time.sleep(0.5)
            continue
        elif player_answer != answer:
            print(Style.DIM + "...\n")
            time.sleep(0.3)
            print("....\n" + Style.RESET_ALL)
            time.sleep(0.3)
            print(
                Fore.RED
                + f"Wrong answer"
                + Style.RESET_ALL)
            print(
                "\nCorrect answer was: "
                + Fore.GREEN
                + f"{answer}\n"
                + Style.RESET_ALL
            )
        break

    if correct_answers == 10:  # Checks if all questions are answered
        score = 10000000
        print("Congratulations! You've won ", end="")
        print(Fore.GREEN + f"${score}\n" + Style.RESET_ALL)
    elif correct_answers >= 1:
        print(f"{player_name}, you've secured at least ", end="")
        print(
            Fore.GREEN
            + f"${prizes[correct_answers -1]}.\n"
            + Style.RESET_ALL)
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
        clear_terminal()
        game_setup()
    elif again == "no":
        clear_terminal()
        # Quit the game after user input
        quit_game()


def quit_game():
    # Function to quit the game
    print(Fore.YELLOW + "Thank you for playing!\n")
    quit()
