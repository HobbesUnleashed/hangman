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
   .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
  | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
  | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
  | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
  | |   |  __  |   | || |   / ____ \   | || |  |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
  | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
  | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
  | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
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
    You have 6 lives remaining''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    You have 5 lives remaining''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    You have 4 lives remaining''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    You have 3 lives remaining''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    You have 2 lives remaining''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    You have 1 life remaining''', '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    You have been hanged!'''
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
    #Ask if the user would like to play
    print("\nWould you like to play? (Y/N)")
    #Receive the user input and convert it to uppercase
    play = input("> ").upper()
    #If the user selects Y for yes
    if play == "Y":
        #Print the following messages - including an option to see the rules
        print("\nGreat! Let's play!")
        print("\nWould you like to see the rules? (Y/N)")
        #Receive the input regarding the rules and convert to uppercase
        rules = input("> ").upper()
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
    else:
        print("\nInvalid input. Please try again.\n")
        intro()

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
    level_choice = input("> ")
    
    #Whatever level they choose (1-5) will return the name of the GoogleSheet that the words are stored on
    if level_choice == "1":
        print("You have selected Simple\n")
        return "simple"
    elif level_choice == "2":
        print("You have selected Easy\n")
        return "easy"
    elif level_choice == "3":
        print("You have selected Intermediate\n")
        return "intermediate"
    elif level_choice == "4":
        print("You have selected Hard\n")
        return "hard"
    elif level_choice == "5":
        print("You have selected Expert\n")
        return "expert"
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

def main():
    #Run the introduction and associated artwork - ask the initial questions of Play? and Rules?
    intro()
    #Store the return value of level_select() to a variable for passing to other functions
    #This tells us which GoogleSheet needs to be accessed for the game selected
    selected_level = level_select()
    #Variable to store the randomly selected word from the selected GoogleSheet
    random_word = get_random_word(selected_level)
    print(random_word)
    #Variable to store the definition of the randomly selected word
    #Function is passed the level/GoogleSheet and the word from it
    definition = get_definition(selected_level, random_word)
    print(definition)

main()