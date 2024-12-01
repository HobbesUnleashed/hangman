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