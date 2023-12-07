## Hangman game

This is my third project among five, where I've crafted a Hangman game to deepen my understanding of Python. Staying true to the traditional rules, the game features a distinctive touch with words and styling that reflects my playful and quirky side, emphasizing my fascination with slightly unusual, old words.

github: https://github.com/Widianne/p3hangman.git

live page: https://lillhanggame-1ce76b01b8a6.herokuapp.com/

I wanted to create something that will give the user nostaliga so hangman it is!

- My code is placed in the `run.py` file 
- My dependencies are placed in the `requirements.txt` file

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Wireframes](#wireframes)
  * [Design process](#design-process)

* [Features](#features)
  * [Rules](#rules)
  * [Play the game](#play-the-quiz)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)
  * [Manual testing](#manual-testing)
  * [Unfixed bugs](#unfixed-bugs)
  * [Additional notes on testing](#additional-notes-on-testing)
  * [Automated testing](#automated-testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Websites visited to gather knowledge](#websites-visited-to-gather-knowledge)
  * [Acknowledgments](#acknowledgments)

---

## **Project Overview**

### **Project Goals**
- Create a game in python
- Understand the concepts of the code written and how the code is executed
- Have no bugs and if there are some have them documented

---

## **User Experience**
- Understand the purpose of the site
- Easy to understand the rules of the game 
- Have fun while getting a response (letters are logged and the man is drawn)
- Mix both hard and easy words
- Long list of words allows the player to play again and again with possibilty to restart game

### **User Expectations**
- Lern new words
- Good visual responsivness so that the user can win
- I want the user to enjoy the game

### **User Stories**

- As a user I want an easy to understand game
- As a user I want to be able to see if I won or lost
- As a user I want to learn new words

---

## **Design**

I've kept it simple to prioritize the game. Incorporating Patorjk decorations with vibrant colors adds an engaging touch to the site, making it visually appealing.

### **Wireframes**

Due to the nature of the project being mostly backend no wireframes were made or needed

### **Design process**

- Colorama module was used for text output color of the terminal
- I keept it simple to focus on the code and my learning

---

### **Rules**

1. The computer selects a random word from a secret list of words.
2. By suggesting letters, you try to guess the right word.
3. You can guess the incorrect letter 6 times before you lose.
4. If you guess a correct letter, it is revealed in the word.
5. For every wrong guess, a part of the hangman is drawn.
6. You win if you guess the word before reaching the maximum incorrect guesses.
7. You lose if you run out of guesses and the hangman is fully drawn.

### **Play the Game**

The program presents rules, prompting users to guess one letter at a time with a dotted line. They have 6 attempts before facing the consequences. As guesses unfold, a running list helps users avoid repetition. Winning and losing outcomes trigger corresponding messages with a restart option.

---

## **Future Implementations**

- more functions, like restart the game mid game
- would be fun to have a more interesting looking hangman 
- fix the oddness in the heruko when it comes to the texts because they r fine in my vscode
- would be fun with some front end design to make it look even better

---
 ## **Technologies Used**

[Colorama](https://pypi.org/project/colorama/) - Used for the colours in the terminal\

### **Languages Used**

Python - Used for the game functionality \

## **Deployment**

The project was deployed on github, the command 'python3 run.py' was used in terminal to launch the game and once there was a good enough portion of the game written it was then deployed on heroku early in the project to avoid problems later on with incompatibility. The following steps were taken for deployment:


1. Add dependencies in requirements.txt file with command "pip3 freeze > requirements.txt"
2. Commit and push to GitHub
3. Go to the Heroku Dashboard
4. Click "Create new app"
5. Name app and select location
5. Add Config Vars for Creds and Port in Settings tab
6. Add the buildbacks to Python and NodeJS in that order
7. Select appropriate deployment method, GitHub
8. Connect to Github and link to repository
9. Enable automatic deployment and/or deploy manually
10. Click on Deploy

---

## **Testing**

### **Manual Testing**

- did several tests in my console and also in heruko to see how it all looked and if it worked
- Also used code validators ws3
- many many attemts but it did work
- the style of the decorative text is lobsided
- used several diffrant styels to try fixing it but did not work so let it be since it does not affect the game.



### **Unfixed bugs**

- it looks lobsided in the heruko but still works so only the style
- used several diffrant styels to try fixing it but did not work so let it be since it does not affect the game.
- user can't restart mid game


 ### **Websites visited to gather knowledge**
  https://stackoverflow.com/questions/75961452/how-do-i-include-an-ascii-art-string-literal-without-getting-syntax-errors-in-py

  https://www.youtube.com/watch?v=pFvSb7cb_Us

  https://www.youtube.com/watch?v=3_CX0aD9Fdg

  https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman

  https://www.youtube.com/watch?v=nkxqRDYFscE
  

