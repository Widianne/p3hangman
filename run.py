"""
imports from necessary libraries
"""
import random
from words import wordDictionary

import colorama 
from colorama import Fore, Back, Style
colorama.init()

"""
the game title 
"""

print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ")
print('''                      
████████╗██╗  ██╗███████╗    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
   ██║   ███████║█████╗      ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝      ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                    
      ''')

"""
the rules of the game
"""

def print_rules():
    print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ \n")
    print("Let's play! Here are the rules:")
    print("1. The computer selects a random word from a secret list of words.")
    print("2. By suggesting letters, you try to guess the right word.")
    print("3. You can guess the incorrect letter 6 times before you lose.")  # Fixed typo here
    print("4. If you guess a correct letter, it is revealed in the word.")
    print("5. For every wrong guess, a part of the hangman is drawn.")
    print("6. You win if you guess the word before reaching the maximum incorrect guesses.")
    print("7. You lose if you run out of guesses and the hangman is fully drawn.\n")
    print("✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ \n")
# call the function to print the rules
print_rules()

"""
the acctual game
"""
# chooses a random word
randomWord = random.choice(wordDictionary)

for letter in randomWord:
    print("_", end=" ")
    
"""
hang man img code that builds the hanged man with every wrong guess, 6 trys until game over
"""

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

"""
this function takes the list of guessed letters and prints the characters of a randomly chosen word, 
revealing guessed letters and hiding the unguessed ones. The function returns the count of 
correctly guessed letters.
"""
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

"""
displays a visual representation of the word, where each letter is represented by a horizontal line
"""
def printlines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

"""
tracks the length of the word, incorrect guesses, current guess index, guessed letters, 
and the count of correct letters guessed
"""
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

"""
prints the guessed letters, prompts the user to guess, stores input in the variable letterGuessed. 
loop continues until either the player makes 6 incorrect guesses or correctly guesses all letters
"""
while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    print("\nGuessed letters: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")

    # Prompt user for input
    letterGuessed = input("\nGuess a lill letter: ")

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

print('''
                                                  (`-')  _ <-. (`-')   (`-')  _                     (`-') (`-')  _   (`-')  
   <-.        .->      <-.           .->    (OO ).-/    \(OO )_  ( OO).-/         .->        _(OO ) ( OO).-/<-.(OO )  
 ,--. )  (`-')----.  ,--. )       ,---(`-') / ,---.  ,--./  ,-.)(,------.    (`-')----. ,--.(_/,-.\(,------.,------,) 
 |  (`-')( OO).-.  ' |  (`-')    '  .-(OO ) | \ /`.\ |   `.'   | |  .---'    ( OO).-.  '\   \ / (_/ |  .---'|   /`. ' 
 |  |OO )( _) | |  | |  |OO )    |  | .-, \ '-'|_.' ||  |'.'|  |(|  '--.     ( _) | |  | \   /   / (|  '--. |  |_.' | 
(|  '__ | \|  |)|  |(|  '__ |    |  | '.(_/(|  .-.  ||  |   |  | |  .--'      \|  |)|  |_ \     /_) |  .--' |  .   .' 
 |     |'  '  '-'  ' |     |'    |  '-'  |  |  | |  ||  |   |  | |  `---.      '  '-'  '\-'\   /    |  `---.|  |\  \  
 `-----'    `-----'  `-----'      `-----'   `--' `--'`--'   `--' `------'       `-----'     `-'     `------'`--' '--' 
      ''')


            

