import random
from words import wordDictionary

data_str = input("enter data here:\n")

print("Let's play Hangman [] ")
print("-------------------------------------------")


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

print("Game Over! Please play again! :)")


            

