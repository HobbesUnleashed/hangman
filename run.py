import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

intro_art = '''
           _______ _       _______ _______ _______ _       
  |\     /(  ___  | (    /(  ____ (       |  ___  | (    /|
  | )   ( | (   ) |  \  ( | (    \/ () () | (   ) |  \  ( |
  | (___) | (___) |   \ | | |     | || || | (___) |   \ | | 
  |  ___  |  ___  | (\ \) | | ____| |(_)| |  ___  | (\ \) |
  | (   ) | (   ) | | \   | | \_  ) |   | | (   ) | | \   |
  | )   ( | )   ( | )  \  | (___) | )   ( | )   ( | )  \  |
  |/     \|/     \|/    )_|_______)/     \|/     \|/    )_)
'''

hangman_art = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    You have 6 lives remaining\n''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    You have 5 lives remaining\n''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    You have 4 lives remaining\n''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    You have 3 lives remaining\n''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    You have 2 lives remaining\n''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    You have 1 life remaining\n''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    You have been hanged!\n'''
]

#The introduction to the game with opening credits
def intro():
    '''
    Provide a welcome screen for the user.
    '''

    print("\nWelcome to\n")
    print(intro_art)
    print("\nA game in which you guess the letters in a word in order to stay alive!!")
    
    #Function to validate the inputs for this function (only Y/N) - with custom user prompts
    def get_valid_input(prompt, error_message):
        while True:
            user_input = input(prompt).upper()
            if user_input in ["Y", "N"]:
                return user_input
            else:
                print(error_message)
    
    #Input and validation
    play = get_valid_input("\nWould you like to play? (Y/N)\n> \n", "\nInvalid input. Please enter 'Y' or 'N'.\n")
    
    if play == "Y":
        print("\nGreat! Let's play!")
        rules = get_valid_input("\nWould you like to see the rules? (Y/N)\n> \n", "\nInvalid input. Please enter 'Y' or 'N'.\n")
        if rules == "Y":
            help()
        else:
            print("\nOkay, let's play!")
    elif play == "N":
        print("\nOkay, maybe next time!")
        exit()

def help():
    '''
    Provide a help screen for the user - detailing the rules of the game.
    '''

    print("\nThe objective of the game is to guess the word before you run out of lives.")
    print("You can guess a letter or the whole word.")
    print("If you guess a letter that is in the word, it will be revealed.")
    print("If you guess a letter that is not in the word, you will lose a life.")
    print("You will not be able to guess the same letter twice - and you will not lose a life for trying to do so")
    print("If you guess the word correctly, you win!")
    print("If you guess the word incorrectly, you lose!")
    print("You have 6 lives. Good luck!")

def level_select():
    '''
    Allow the user to select a level of difficulty.
    '''

    levels = {
        "1": "simple",
        "2": "easy",
        "3": "intermediate",
        "4": "hard",
        "5": "expert"
    }
    
    print("\nThere are a number of difficulty levels for you to choose from")
    print("\nSelect your level (1-5):\n")
    for num, level in levels.items():
        print(f"Level {num}. {level.capitalize()}")
    print("Enter 'E' to exit")

    level_choice = input("> \n").upper()
    
    if level_choice in levels:
        print(f"You have selected {levels[level_choice].capitalize()}\n")
        play_game(levels[level_choice])
    elif level_choice == "E":
        print("\nThank you for playing. Goodbye :)")
        exit()
    else:
        print("Invalid input. Please select level 1-5\n")
        return level_select()

def get_random_word(level):
    '''
    Get a random word from the specified worksheet.
    
    Args:
        level (str): The difficulty level selected by the user.
        
    Returns:
        str: A random word from the specified worksheet.
    '''
    
    worksheet = SHEET.worksheet(level)
    words = worksheet.col_values(1)[1:]
    return random.choice(words).lower()

def get_definition(level, word):
    '''
    Get the definition of a word from the specified worksheet.
    
    Args:
        level (str): The difficulty level selected by the user.
        word (str): The word for which to get the definition.
        
    Returns:
        str: The definition of the word.
    '''
    
    worksheet = SHEET.worksheet(level)
    rows = worksheet.get_all_values()[1:]
    
    for row in rows:
        if row[0].lower() == word:
            return row[1]

def display_dashes(word, correct_guesses):
    '''
    Display dashes corresponding to the length of the word with correctly guessed letters
    
    Args:
        word (str): The word for which dashes are to be displayed.
        correct_guesses (list): List of correctly guessed letters.
        
    Returns:
        str: A string with dashes and correctly guessed letters, with spaces between each character.
    '''
    
    return ' '.join([letter if letter in correct_guesses else '-' for letter in word])

def play_game(level):
    '''
    Play the hangman game with the given random word.
    
    Args:
        level (str): The difficulty level selected by the user.  
        
    Returns:
        None
    '''
    
    #Function to get a new word and definition for repeat games
    def get_new_random_word_and_definition(level):
        random_word = get_random_word(level)
        definition = get_definition(level, random_word)
        return random_word, definition
    
    random_word, definition = get_new_random_word_and_definition(level)
    
    correct_guesses = []
    incorrect_guesses = []
    
    while True:
        current_display = display_dashes(random_word, correct_guesses)
        print(f"\nCurrent word: {current_display}")
        print(hangman_art[len(incorrect_guesses)])
        
        if incorrect_guesses:
            print(f'You have already guessed {incorrect_guesses}')
        
        guess = input("\nGuess a letter: \n").lower()
        
        #Check if input is valid - single digit, not a number
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single letter.")
            continue
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("\nYou have already guessed that letter. Try again.")
            continue
        
        if guess in random_word:
            correct_guesses.append(guess)
            print(f"\nGood job! {guess} is in the word.")
            
            if all(letter in correct_guesses for letter in random_word):
                print(f"\nCongratulations!\nYou guessed the word: {random_word}")
                print(f'The definition of this word is: {definition}')
                break
        else:
            incorrect_guesses.append(guess)
            print(f"\nSorry, {guess} is not in the word.")
            
            if len(incorrect_guesses) >= 6:
                print(hangman_art[-1])
                print(f"\nGame over! You ran out of lives.\nThe word was: {random_word}")
                print(f'The definition of this word is: {definition}')
                break
    
    #Give the user the chance to play again, change level or exit
    while True:
        choice = input("\nWould you like to play again at the same level (P), return to level select (L) or exit the game (E)?\n> \n").upper()
        
        if choice == "P":
            new_random_word, new_definition = get_new_random_word_and_definition(level)
            play_game(level)
            break
        elif choice == "L":
            level_select()
            break
        elif choice == "E":
            print("\nThank you for playing. Goodbye :)")
            exit()
        else:
            print("\nInvalid input. Please enter 'P' to play again or 'L' to return to level select or 'E' to exit the game")

def main():
    intro()
    level_select()
    
main()