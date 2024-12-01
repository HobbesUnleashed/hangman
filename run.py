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
    print("Welcome to\n")
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

def main():
    intro()

main()