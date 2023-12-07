import random #imports from necessary libraries
import colorama
from words import wordDictionary

from colorama import Fore, Style
colorama.init()

"""
the game title 
"""

print(Fore.RED + "✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ✧.* ˚ ✦ ")
print('''                      
█╗  ██╗ █████╗ ███╗   ██╗ ██████╗     ████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝     ╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗       ██║   ███████║█████╗      ██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║       ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝       ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                                                   
      ''')


def print_rules():
    """
    Prints the rules
    """
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
    print(Style.RESET_ALL)
# call the function to print the rules


"""
the actual game
"""


def get_word():
    """
    Gets a random word
    """
    return random.choice(wordDictionary)


def print_word(guessed_letters, random_word):
    """
    Prints the word
    """
    counter = 0
    right_letters = 0
    for char in random_word:
        if char in guessed_letters:
            print(random_word[counter], end=" ")
            right_letters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return right_letters


def print_lines(random_word):
    """
    Prints lines for word
    """
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")


def play_game():
    """
    Gets a random word and plays the core game loop
    """
    random_word = get_word()
    
    for letter in random_word:
        print("_", end=" ")

    length_of_word_to_guess = len(random_word)
    amount_of_times_wrong = 0
    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0

    while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
        print("\nGuessed letters: ")
        for letter in current_letters_guessed:
            print(letter, end=" ")
        

        # Prompt user for input
        letter_guessed = input("\nGuess a lill letter: ")

        if not letter_guessed.isalpha() or len(letter_guessed) > 1 or len(letter_guessed) == 0:
            print('Only one letter at a time!')
            continue

        if  current_guess_index < len(random_word) and letter_guessed == random_word[current_guess_index]:
            current_letters_guessed.append(letter_guessed)
            current_guess_index += 1
            current_letters_right = print_word(
                current_letters_guessed, random_word)
            print_lines(random_word)
    
            
        else:
            amount_of_times_wrong += 1
            print_hangman(amount_of_times_wrong)
            current_letters_guessed.append(letter_guessed)
            current_letters_right = print_word(
                current_letters_guessed, random_word)
            print_lines(random_word)
            
    if current_letters_right == length_of_word_to_guess:
        print("Good job! You guessed the word. You get a potato!")
       
        # Check if the game is not over due to winning
    if current_letters_right != length_of_word_to_guess: 
        print("""
                                                  (`-')  _ <-. (`-')   (`-')  _                     (`-') (`-')  _   (`-')  
   <-.        .->      <-.           .->    (OO ).-/    \(OO )_  ( OO).-/         .->        _(OO ) ( OO).-/<-.(OO )  
 ,--. )  (`-')----.  ,--. )       ,---(`-') / ,---.  ,--./  ,-.)(,------.    (`-')----. ,--.(_/,-.\(,------.,------,) 
 |  (`-')( OO).-.  ' |  (`-')    '  .-(OO ) | \ /`.\ |   `.'   | |  .---'    ( OO).-.  '\   \ / (_/ |  .---'|   /`. ' 
 |  |OO )( _) | |  | |  |OO )    |  | .-, \ '-'|_.' ||  |'.'|  |(|  '--.     ( _) | |  | \   /   / (|  '--. |  |_.' | 
(|  '__ | \|  |)|  |(|  '__ |    |  | '.(_/(|  .-.  ||  |   |  | |  .--'      \|  |)|  |_ \     /_) |  .--' |  .   .' 
 |     |'  '  '-'  ' |     |'    |  '-'  |  |  | |  ||  |   |  | |  `---.      '  '-'  '\-'\   /    |  `---.|  |\  \  
 `-----'    `-----'  `-----'      `-----'   `--' `--'`--'   `--' `------'       `-----'     `-'     `------'`--' '--' 
      """)
    
    
             
    
    restart = input('press Y to restart')
    if restart.lower() == 'y':
        play_game()


def print_hangman(wrong):
    """
    Prints hangman graphic
    """
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


def main():
    """
    initial game build
    """
    print_rules()
    play_game()


main()