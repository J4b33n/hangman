import random

word_list = ['apple', 'banana', 'orange', 'pear', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'melon']

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.word = self.word.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
            print(f"Word: {' '.join(self.word_guessed)}")
            if self.num_letters == 0:
                print(f"You win! Lives left: {self.num_lives}")
                print(f"The word was: {self.word}")
                print("Starting a new game...")
                self.word = random.choice(self.word_list)
                self.word_guessed = ['_'] * len(self.word)
                self.num_letters = len(set(self.word))
                self.num_lives = 5
                self.list_of_guesses = []
                self.ask_for_input()
        else:
            print(f"Bad luck! {guess} is not in the word.")
            self.num_lives -= 1
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)

def play_game(word_list, num_lives):
    game = Hangman(word_list)
    game.ask_for_input()

play_game(word_list, 6)