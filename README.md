
# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone_3.py
This code contains two functions: ask_for_input() and check_guess().

`ask_for_input()`
This function prompts the user to guess a letter and validates their input. It ensures that the user enters a single alphabetical character. Once a valid input is received, it calls the check_guess() function to check if the guess is in the word.

`check_guess()`
This function takes a guess as input and converts it to lowercase. It then checks if the guess is in the word and provides appropriate feedback to the user. If the guess is correct, it informs the user that the guess is in the word. Otherwise, it indicates that the guess is not in the word and encourages the user to try again.

# Milestone_4.py
Hangman
This class implements the classic Hangman game.

## Usage
Python
```
from hangman import Hangman

word_list = ["apple", "banana", "orange"]
game = Hangman(word_list)
game.ask_for_input()
```
## Methods
`__init__(self, word_list, num_lives=5)`
Initializes the game with a list of words and a number of lives.

`word_list`: A list of words that the game can choose from.
`num_lives`: The number of lives the player has before they lose the game.
`check_guess(self, guess)`
Checks whether the guessed letter is in the word.

`guess`: The letter the player guesses.
`ask_for_input(self)`
Prompts the player to guess a letter.

## Attributes
`word`: The word that the player is trying to guess.
`word_guessed`: A list of letters that the player has guessed correctly.
`num_letters`: The number of letters in the word.
`num_lives`: The number of lives the player has left.
`word_list`: A list of all the words that the game can choose from.
`list_of_guesses`: A list of all the letters that the player has guessed.