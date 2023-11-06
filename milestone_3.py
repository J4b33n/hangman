# Create a new script called milestone_3.py. This file will contain the code for this milestone.
word = "hangman"
# Step 1:
# Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.
while True:
    # Step 2:
    # Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")
    # Step 3:
    # Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
    if guess.isalpha() and len(guess) == 1:
        # Step 4:
        # If the guess passes the checks, break out of the loop.
        break
    # Step 5:
    # If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Step 1:
# Create an if statement that checks if the guess is in the word.
if guess in word:
    # Step 2:
    # In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.
    print(f"Good guess! {guess} is in the word.")
# Step 3:
# Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

# Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.
# Step 1:
# Define a function called check_guess. pass in the guess as a parameter for the function.
# Write the code for the following steps in the body of this function.
# The check_guess function will take the guessed letter as an argument and check if the letter is in the word.
def check_guess(guess):
    # Step 2:
    # Convert the guess into lower case.
    guess = guess.lower()
    # Step 3:
    # Move the code that you wrote to check if the guess is in the word into this function block.
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# The ask_for_input function.
def ask_for_input():
    # Step 1:
    # Define a function called ask_for_input.
    # Write the code for the following steps in the body of this function.
    # Step 2:
    # Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    # Step 3:
    # Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.
    check_guess(guess)
