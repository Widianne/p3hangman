import random
from words import wordDictionary

import colorama 
from colorama import Fore, Back, Style
colorama.init()

print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦  ")
print('''                        
 _/\/\____/\/\_____________________________________________________________________________
    _/\/\____/\/\__/\/\/\______/\/\/\/\______/\/\/\/\__/\/\/\__/\/\____/\/\/\______/\/\/\/\___ 
   _/\/\/\/\/\/\______/\/\____/\/\__/\/\__/\/\__/\/\__/\/\/\/\/\/\/\______/\/\____/\/\__/\/\_  
  _/\/\____/\/\__/\/\/\/\____/\/\__/\/\____/\/\/\/\__/\/\__/\__/\/\__/\/\/\/\____/\/\__/\/\_   
 _/\/\____/\/\__/\/\/\/\/\__/\/\__/\/\________/\/\__/\/\______/\/\__/\/\/\/\/\__/\/\__/\/\_    
_______________________________________/\/\/\/\___________________________________________       
      ''')
def print_rules():
    print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦  ")
    print("Let's play! Here are the rules:")
    print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦  ")
    print("1. The computer selects a random word.")
    print("2. By suggesting letters you try to guess the right word.")
    print("3. You can guess the incorrect letter 6 times before you die).")
    print("4. If you guess a correct letter, it is revealed in the word.")
    print("5. For every wrong guess a part of the hangman is drawn.")
    print("6. You win if you guess the word before reaching the maximum incorrect guesses.")
    print("7. You lose if you run out of guesses and the hangman is fully drawn.")
    print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦  \n")
 
 
# Call the function to print the rules
print_rules()


# Choose a random word
randomWord = random.choice(wordDictionary)

for letter in randomWord:
    print("_", end=" ")

def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\\ |")
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\\ |")
        print("/   |")
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("    ===")

def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters

def printlines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")

    # Prompt user for input
    letterGuessed = input("\nGuess a little letter: ")

    # Check if the letter is correct
    if current_guess_index < len(randomWord) and letterGuessed == randomWord[current_guess_index]:
        current_letters_guessed.append(letterGuessed)
        current_guess_index += 1
        current_letters_right = printWord(current_letters_guessed)
        printlines()
    else:
        amount_of_times_wrong += 1
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printlines()

print("Game Over! Play again ! :)")


            

