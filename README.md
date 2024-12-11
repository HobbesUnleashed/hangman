# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with the user having the option to read the rules and select a difficulty level, ranging from simple to expert.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen](     )

[View Hangman live project here](https://hangmansl-6787a9f8901b.herokuapp.com/)
- - -

## Table of Contents
### [How to play](#how-to-play-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to Play

In this implementation of Hangman, you will play against the computer. 
You will be prompted to choose a difficulty level (simple, easy, intermediate, hard or expert), and the computer will randomly select a word from a list of words corresponding to that level. 
You will then have to guess the letters in the chosen word before the hangman is complete.

## Logic flowchart

![Flowchart](      )

## User Experience (UX)

Hangman is a classic word guessing game that provides a simple yet entertaining user experience. The user is presented with a blank series of dashes that represent the letters of a mystery word. They have to guess the letters in the word, one at a time. With each correct guess, the letter is revealed in the corresponding position(s). However, with each incorrect guess, a part of a hangman's body is drawn. The user can guess until they either correctly guess the entire word or the hangman is fully drawn, resulting in a loss. The game is easy to learn and provides a good balance of challenge and reward. It is also a great way to improve vocabulary and spelling skills, along with learning the definitions of the words you guess - all while having fun.

### User Stories

* First-time visitor goals
    * Understand how the game works. Clear instructions and what the objective of the game is.
    * Play the game. Once the user understands the game, they will likely want to play it.
    * Enjoy the experience. The hangman game should be engaging and fun for the user.

* Returning visitor goals
    * Continue playing. The returning visitor may have enjoyed playing the game and wants to play again.
    * Share with friends. Inviting friends to give the game a try.
    * Exploring new features, if there are any.

* Frequent user goals
    * Improving their speed and accuracy in guessing words.
    * Learning the definitions of further words that they are presented with.
    * Increasing the difficulty level of the game to challenge themselves.
    * Sharing the game with others or inviting friends to play.
    * Exploring new features, if there are any.

---

## Features

* Word selection. The game randomly selects a word from one of the five available predefined lists of words.
* Difficulty settings. The game offers three difficulty settings, simple, easy, intermediate, hard and expert.
* Words are stored in a Google Sheet, each level of difficulty on a sheet of their own.
* Visual interface. Appealing interface that is easy to navigate and understand.
* Letter input. User can input their guess letter by letter to guess the hidden word.
* Incorrect guess tracking. Visually drawing a part of the hangman figure.
* Win or loss detection. Detect when the player has either successfully guessed the entire word or made too many incorrect guesses and lost the game.
* Play again at the end of the game - either at the same level of difficulty or choose another level.
* Google sheets storing the selection of words and definitions, broken into separate worksheets for differing levels.
* [View Google sheets here] (https://docs.google.com/spreadsheets/d/1vXybG0I9jpkprSMuWqsz2x6YCyv8aFziE9TtcZA-gNc/edit?usp=sharing)

### Existing Features

* Intro screen
    * Displays logo and a welcome message.

![Intro Screen](        )

* Rules
    * User can choose to display rules or skip them using "y" or "n".

![Rules](       )

* Introduction message and difficulty setting

![Difficulty Setting](       )

* Prompt user to make a guess

![Guess a letter](         )

* Correct Guess
    * If letter is guessed, "Correct" message displays.

![Correct guess](         )

* Incorrect Guess
    * If letter is not guessed, "Incorrect" message displays.

![Incorrect guess] (             )

* User guesses the word correctly
    * Message that confirms hangman is beaten.

![Won game](           )

* User is out of guesses
    * Message that confirms a lost game.

![Lose](           )

* Play again, choose level or exit

![Play again](          )

## Features Left to Implement

* Additional words might be available.
* Different word topics
* Scoring system
* Two player option

---

## Design

* Icons
    * Hangman logo
    * Hangman figures

* Flowchart
    * [Draw.io](          )

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Codeanywhere](https://app.codeanywhere.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.

## Testing 

CI Python Linter was used to test run.py, colors.py and hangman_art_words.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](         )
</details>

## Manual Testing

The game was manually tested extensively using codeanywhere terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end. Testing of rules display, select difficulty input validation, gallows ASCII image display, correct and incorrect answers and finally win or lose display, play again and change level features.



| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | -------------- | ----------- | ------------- | ---------- |
| Intro Screen   | To display logo and welcome message | None | As Expected | ![Intro Screen](        ) |
| Display Rules | To display rules or skip them using either "y" or "n" | Input "y" to display, input "n" to skip | As Expected | ![Display rules](         ) |
| Select Difficulty   | To retrieve word from the selected difficulty option | Input simple, easy, intermediate, hard or expert | As Expected | ![Difficulty](           ) |
| Guess a letter   | Prompts user to guess a letter | Input a letter guess | As Expected | ![Guess a letter](           ) |
| Guess Correct   | To display correct, gallows with no penalty applied, a list of already guessed letters and updated hidden word | Guessed a correct letter | As Expected | ![Guess correct](           ) |
| Guess Incorrect   | To display incorrect, gallows with penalty applied, a list of already guessed letters and updated hidden word | Guessed an incorrect letter | As Expected | ![Guess incorrect](          ) |
| Guess Invalid   | To display a message saying to input a single letter | Invalid input such as e.g too many letters or a number | As Expected | ![Guess invalid](          ) |
| Guessed Already   | To display a message saying guessed already | Input a letter that was already tried  | As Expected | ![Guess invalid](       ) |
| Hangman gallows   | To display and update hangman gallows | Input a letter guess  | As Expected | ![Gallows](        ) |
| Win   | To display win message | Guess the word in less than six tries | As Expected | ![Win game](         ) |
| Lose   | To display lose message | Fail to guess the word in six tries | As Expected | ![Lose game](          ) |
| Play Again   | To display play again | Choose "p" for new game, "l" for level selection or "e" to exit the game | As Expected | ![Play again](          ) |
| Google Sheets   | To access words for various levels | Not accessed directly in the game | As Expected | ![Google Sheets](          ) |

## Input validation testing

* Display rules
    * Cannot continue with empty input
    * Must be "y" or "n"

![Rules validation](          )

* Select difficuly
    * Cannot continue with empty input
    * Must be "1" for simple, "2" for easy, "3" for intermediate, "4" for hard or "5" for expert

![Difficulty validation](            )

* Guess a letter
    * Cannot continue with empty input
    * Must be a single letter
    * Must be a letter

![Letter validation](         )

* Play again
    * Cannot continue with empty input
    * Must be "p", "l" or "e"

![Play again validation](            )

## Fixed Bugs

* There is a warning notice that informs the user that there is just one chance remaining if he reaches his fifth guess before attempting to use a last guess. This meant that even if the user correctly identified the final letter after receiving a warning after his fifth guess and so winning the game, the warning message would still appear.
* This bug was fixed in the play_game function which was refactored to keep track of the is_game_won function in the code that runs the warning, final chance message, which can be found in the commits history.
* This bug was indentified by playing the game multiple times and trying to get to all possible outcomes that a user might experience while playing the game.

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Hangman](           )

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository hangman](https://github.com/HobbesUnleashed/hangman)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository hangman] (https://github.com/HobbesUnleashed/hangman)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons.
* I gained more python concepts through Python for begginers written by Brady Ellison.
* Python 3.11.3 documentation.
* MDN web docs for python [Documentation](https://developer.mozilla.org/en-US/docs/Glossary/Python).

### Content

* Hangman game.
* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.