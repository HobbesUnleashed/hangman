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

#Intro-art generated from https://patorjk.com/software/taag/#p=display&c=vb&f=Blocks&t=Hangman
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

#Hangman_art copied from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
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

def intro():
    '''
    Provide a welcome screen for the user.
    '''
    print("\nWelcome to\n")
    #Print the games introduction art
    print(intro_art)
    #Print a blurb to the game
    print("\nA game in which you guess the letters in a word in order to stay alive!!")

    #Function to get valid input (Y/N)
    def get_valid_input(prompt, error_message):
        while True:
            user_input = input(prompt).upper()
            if user_input in ["Y", "N"]:
                return user_input
            else:
                print(error_message)

    #Ask if the user would like to play
    print("\nWould you like to play? (Y/N)\n")
    #Receive the user input and convert it to uppercase
    play = get_valid_input("> \n","\nInvalid input. Please enter 'Y' or 'N'.\nWould you like to play?")
    #play = input("> \n").upper()
    #If the user selects Y for yes
    if play == "Y":
        #Print the following messages - including an option to see the rules
        print("\nGreat! Let's play!\n")
        print("\nWould you like to see the rules? (Y/N)\n") 
        #Receive the input regarding the rules and convert to uppercase
        rules = get_valid_input("> \n", "\nInvalid input. Please enter 'Y' or 'N'.\nWould you like to see the rules?")
        #rules = input("> \n").upper()
        #If the user selects Y for yes
        if rules == "Y":
            #Run the help function which details the rules
            help()
        #Otherwise
        else:
            #Print this message and load the next function from main()
            print("\nOkay, let's play!")

    #If user selects N for no in relation to playing the game
    elif play == "N":
        #Print this message and then exit the runtime
        print("\nOkay, maybe next time!")
        exit()
    #Otherwise - any other input will receive this message and the intro() function will begin again
    '''else:
        print("\nInvalid input. Please try again.\n")
        intro()'''

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
    print("\nThere are a number of difficulty levels for you to choose from - these are listed below!")
    print("\nPlease select a level of difficulty (enter the number of the level you want to select - e.g 1 for the simple level):")
    print("Level 1. Simple (a word of 3 letters)")
    print("Level 2. Easy (either a 4 or 5 letter word)")
    print("Level 3. Intermediate (either a 6 or 7 letter word)")
    print("Level 4. Hard (either an 8 or 9 letter word)")
    print("Level 5. Expert (a word of 10 letters or more)\n")
    
    #Ask for the user choice
    level_choice = input("> \n")
    
    #Whatever level they choose (1-5) will return the name of the GoogleSheet that the words are stored on
    if level_choice == "1":
        print("You have selected Simple\n")
        play_game("simple")
    elif level_choice == "2":
        print("You have selected Easy\n")
        play_game("easy")
    elif level_choice == "3":
        print("You have selected Intermediate\n")
        play_game("intermediate")
    elif level_choice == "4":
        print("You have selected Hard\n")
        play_game("hard")
    elif level_choice == "5":
        print("You have selected Expert\n")
        play_game("expert")
    #If an option outside of numbers 1-5 is selected the error message is displayed and the level_select() function is re-run
    else:
        print("Invalid input. Please try again.\n")
        return level_select()

def get_random_word(level):
    '''
    Get a random word from the specified worksheet.
    
    Args:
        level (str): The difficulty level selected by the user.
        
    Returns:
        str: A random word from the specified worksheet.
    '''

    #Local variable which accesses the relevant GoogleSheet by passing the parameter of level
    worksheet = SHEET.worksheet(level)
    #Get all values in the first column, excluding the header
    words = worksheet.col_values(1)[1:]
    #Return a random word in lowercase
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

    #Local variable which accesses the relevant GoogleSheet by passing the parameter of level
    worksheet = SHEET.worksheet(level)
    #Get all values in the worksheet, excluding the header
    rows = worksheet.get_all_values()[1:]
    #Find the row with the specified word and return its definition
    #Goes through each row of data
    for row in rows:
        #If the row - converted to lowercase - matches the randomly selected word
        if row[0].lower() == word:
            #Returns the definition
            return row[1]

def display_dashes(word, correct_guesses):
    '''
    Display dashes corresponding to the length of the word with correctly guessed letters.
    
    Args:
        word (str): The word for which dashes are to be displayed.
        correct_guesses (list): List of correctly guessed letters.
        
    Returns:
        str: A string with dashes and correctly guessed letters, with spaces between each character.
    '''

    #Local variable set to an empty string - will be populated by the function
    display = ''
    #Go through each letter in the random word
    for letter in word:
        #If the letter appears in the word
        if letter in correct_guesses:
            #Display the local variable, the correct letter (in the correct spot) and a space after each instance
            display += letter + ' '
        #Otherwise, for every letter that appears in the word, set a - and space to the local variable
        else:
            display += '- '
    #Returns the word without any spaces in it for final display
    return display.strip()

def play_game(level):
    '''
    Play the hangman game with the given random word.
    
    Args:
        level (str): The difficulty level selected by the user.
        
    Returns:
        None
    '''

    #Function to get a new random word and definition
    def get_new_random_word_and_definition(level):
        random_word = get_random_word(level)
        definition = get_definition(level, random_word)
        return random_word, definition

    #Get the initial random word and definition
    random_word, definition = get_new_random_word_and_definition(level)

    #Local variables to store an array of values as labelled
    correct_guesses = []
    incorrect_guesses = []
    
    while True:

        #Display current state of dashes
        current_display = display_dashes(random_word, correct_guesses)
        print(f"\nCurrent word: {current_display}")

        #Display hangman stage
        #Uses the array of hangman_art and references against the number of incorrect guesses
        #Then displays the index number of hangman_art that matches the number of incorrect guesses - this comes from later in function
        print(hangman_art[len(incorrect_guesses)])

        if incorrect_guesses != []:
            print(f'You have already guessed {incorrect_guesses}')
        else:
            print('\n')
        
        #Get user's guess and convert to lowercase
        guess = input("\nGuess a letter: \n").lower()
        
        #Check if guess is valid
        #Make sure the guess is one character long and is not a number
        #Prints an error if either is incorrect
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single letter.")
            continue
        
        #Check if guess has already been made
        #Checks against both the correctly and incorrectly made previous guesses
        if guess in correct_guesses or guess in incorrect_guesses:
            print("\nYou have already guessed that letter. Try again.")
            continue
        
        #Check if guess is correct
        if guess in random_word:
            #Add the letter to the correct_guesses array and print message
            correct_guesses.append(guess)
            print(f"\nGood job! {guess} is in the word.")
            
            #Check if user has guessed all letters
            if all(letter in correct_guesses for letter in random_word):
                print(f"\nCongratulations!\nYou guessed the word: {random_word}")
                print(f'The definition of this word is: {definition}')
                break
        #Checks if guess is incorrect
        else:
            #Add the letter to the incorrect_guesses array and print message
            incorrect_guesses.append(guess)
            print(f"\nSorry, {guess} is not in the word.")
            
            #Check if user has run out of lives - maximum of 6
            #If incorrect_guesses array has 6 or more values
            if len(incorrect_guesses) >= 6:
                #Print the hangman_art of this length -1 to match the array
                print(hangman_art[-1])
                #Print the following messages so the user knows the game is lost, what the word is and the definition of it
                print(f"\nGame over! You ran out of lives.\nThe word was: {random_word}")
                print(f'The definition of this word is: {definition}')
                break
    
    # Ask the user if they want to play again or return to level select or exit
    while True:
        print("\nWould you like to play again at the same level (P), return to level select (L) or exit the game (E)?")
        choice = input("> \n").upper()
        if choice == "P":
            #Select a new random word and definition
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
    #Run the introduction and associated artwork - ask the initial questions of Play? and Rules?
    intro()
    #Store the return value of level_select() to a variable for passing to other functions
    #This tells us which GoogleSheet needs to be accessed for the game selected
    selected_level = level_select()
    #Variable to store the randomly selected word from the selected GoogleSheet
    random_word = get_random_word(selected_level)
    #Variable to store the definition of the randomly selected word
    #Function is passed the level/GoogleSheet and the word from it
    definition = get_definition(selected_level, random_word)
    #Function to run the game and receives the random word and it's definition
    play_game(selected_level)

#Runs the main() function which holds and activates the other program functions as needed
main()