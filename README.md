# Who Wants to Be a Millionaire Quiz

## Introduction

The "Who Wants to Be a Millionaire Quiz" is a browser-based quiz game developed with Python. It's a quiz game that offers multiple-choice questions, and players earn money for each correct answer.

This game was developed in Python for use in the terminal and utilizes the Code Institute Python Template to create a "terminal" interface within a web browser.

View the live website on [Heroku](#) <!-- Add your Heroku link here -->

## UX

### The Strategy Plane

The game is designed to be a fun, knowledge-based quiz that people can enjoy on their chosen difficulty level and have their scores recorded in a spreadsheet. It's suitable for individual users looking to play a game for short or medium periods of time. To enhance the experience, the colorama library was used to add visual appeal to the terminal interface.

#### Site Goals

The goals of the site are as follows:

* Provide users with a fun and simple-to-play quiz.
* Offer users the option to choose their preferred difficulty level.
* Allow users to access a leaderboard to see their ranking compared to other players.

#### User Stories

User stories include:

* As a user, I want a quiz to practice and test my knowledge.
* As a user, I want the ability to choose the game difficulty.
* As a user, I want to compare my results with other players.

#### The Scope Plane

**Planned Features:**

* A menu with a selection screen at the start of the game.
* A selection screen containing 'Play,' 'Rules,' and 'Highscore' options.
* Name input and difficulty selection with three modes.
* Game interface during the quiz to display the current score, player name, and difficulty.
* An option to play again.
* A highscore board for each difficulty level.

### The Structure Plane

**User Story:**

As a user, I want a fun and simple quiz to test my knowledge.

**Acceptance Criteria:**

* It should be clear to the user that this is a quiz with a highscore board.

**User Story:**

As a user, I want to be able to check my score and compare it to other players.

**Acceptance Criteria:**

* The user should have the option to check the highscore board.

### The Skeleton Plane

#### Wireframe Mock-Ups

Due to the limited options for customizing the terminal-based game, colorama was used to provide UX design.

### Logic Flow

To develop the logical steps required within the quiz, and to understand how the different functions within the quiz logic elements would interact, a flow chart was created detailing the individual steps for the game. The game logic can be broken down into main sections: initial startup, select screen, and game loop.

![Logic Flow](/documentation/game-flow.png)

### Game Loop

The game loop begins after the user inputs their name and difficulty. It iterates through a dictionary of questions stored in a separate file until all questions are answered or an incorrect answer is provided. Various return methods are used to pass specific user data into other functions.

![Game Loop](/documentation/round-flow.png)

### The Surface Plane

#### Design

A game interface was created to allow users to keep track of their current score and difficulty, which is later written to a Google Sheet for the highscore board.

### Features

#### Welcome Screen

At the start of the game, the user is presented with a menu consisting of 'Play,' 'Rules,' and 'Highscore' options.

![Welcome Screen](/documentation/start-screen.png)

#### Rules Screen

If users select the 'Rules' option from the main menu, the screen displays the objective of the game.

![Rules Screen](/documentation/rules.png)

#### Highscore Screen

Choosing the 'Highscore' option displays the top 5 highscores for each difficulty level.

![Highscore Screen](/documentation/highscore-board.png)

#### Play Option

Selecting the 'Play' option initiates the game and prompts the user for their name and difficulty level.

![Play Screen](/documentation/difficulty.png)

#### Name Option

Users can enter their name, and if not, the name is defaulted to "None."

![Name Screen](/documentation/name.png)

#### Question Generation

Once the name and difficulty are input, the game loop begins, generating questions from a separate file.
Questions are displayed along with answer choices "A), B), C), and D)," and players can input their answer.

![Choice](/documentation/choice.png)

The code checks the player's answer and responds accordingly, either increasing the score for correct answers or showing the correct answer for incorrect ones.

![Correct Answer](/documentation/correct-answer.png)
![Wrong Answer](/documentation/wrong-play.png)

After the game ends, the player's name, difficulty, and score are added to a Google Sheet. This dynamic highscore board updates in real-time based on player input.

## Future Enhancements

In the future, lifeline support will be added to the game along with design improvements.

## Testing

The code was tested using a CI Python linter to ensure its quality. The linter reported no issues, indicating that the code is well-structured and adheres to coding standards.

## Manual Testing

The application has been manually tested to ensure it functions correctly and provides a smooth user experience. The following scenarios were tested:

### Gameplay

1. **Question Display**: Checked if questions are displayed correctly.
2. **Answer Input**: Entered valid answers (A, B, C, D) and ensured they were accepted.
3. **Invalid Answer Input**: Entered invalid answers and verified that error messages were shown and players were prompted to enter valid answers.
4. **Correct Answers**: Ensured that correct answers resulted in a score increase.
5. **Incorrect Answers**: Verified that incorrect answers were handled correctly, and the correct answer was displayed.
6. **Game Completion**: Checked if the game ends when the player answers all questions or chooses to quit.
7. **Play Again**: Confirmed that the "Play Again" feature works as expected.

These manual tests ensure that the application functions as intended and provides a user-friendly experience while handling errors gracefully.

## Error Handling Testing

The application includes robust error handling to provide a smooth user experience. Here are some examples of how the code handles errors:

### Player's Answer Input

The code handles errors when the player enters an invalid choice for answers during the game. If the player doesn't input 'A,' 'B,' 'C,' or 'D,' they will receive an error message and be prompted to enter a valid choice. The code repeats the prompt until a valid answer is provided.

### Rules Selection Input

If a player enters an invalid option while choosing between "Play," "Rules," or "Highscore," the code handles it gracefully. The player will receive an error message and be prompted to enter a valid option.

### Player Name Input

The code allows players to input their names but handles the case where a player provides an empty name. It will replace the empty input with 'None.'

### Difficulty Selection Input

While choosing the difficulty level, players must enter 'Easy,' 'Normal,' or 'Hard.' If an invalid option is provided, an error message is shown, and the player is asked to enter a valid difficulty level.

### Play Again Input

After completing the game, players can choose whether to play again or not. If the player enters an invalid option, they will receive an error message and be prompted to enter a valid response.

These error handling features ensure that players can interact with the application smoothly and handle various scenarios where user input may not be as expected.

## Libraries Utilized

### Built-in Python Libraries

The application makes use of several built-in Python libraries to enhance its functionality.

#### Random

The `random` library is employed to shuffle the questions, ensuring that they are presented in a randomized order.

#### Time

The `time` library is utilized to incorporate time delays within the program. These delays simulate the time between a player's input, their points increasing, and the display of correct or wrong messages before the next question is presented. This feature enhances the overall gameplay experience.

#### os

The `os` library is imported to take advantage of `os.system` and `os.name` functionalities. These features allow the application to clear the terminal screen, providing a cleaner and more structured interface for the user.

#### GSpread

The application also incorporates the `gspread` library to establish a connection with the Google Sheets API. This integration enables the creation of a live leaderboard that updates in real-time based on every player's input. This dynamic leaderboard adds an interactive and competitive element to the game, making it more engaging for users.

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Heroku Link](#)

Install the following:

1: how to download just the packages required for this project (pip3 install -r requirements.txt)
and
2: how to freeze the commands for a local copy of this project on their own account (pip3 freeze --local > requirements.txt)

## Credits

#### Code

I was assisted and advised to use colorama for styling by my mentor, Matt Bodden.

### Content

#### YouTube

[YouTube](https://www.youtube.com/watch?v=bu5wXjz2KvU&t=577s) was used for better understanding and implementation of Google sheets with Python.

#### Stack Overflow

[Stack Overflow](https://stackoverflow.com/questions/68859429/how-to-append-data-in-a-googlesheet-using-python) was useful while I developed my understanding of appending data to Google sheet.

#### Copy Programming

[Copy Programming](https://copyprogramming.com/howto/python-sort-data-in-python-using-lambda) site was used for better understanding of sorting data in the Google sheet using Python.

### Acknowledgements

I'd like to thank the following:

* My mentor Matt Bodden for supporting me and assisting me with useful coding skills and knowledge.
* Matt Bodden for helping with the planning of game logic, suggesting modules and how to improve certain aspects of the development process.
* I'd like to extend my gratitude to my friends who provided guidance and assistance with certain aspects of the code, including the use of lambda functions.
