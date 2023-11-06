import random

# Step 1:
# Create a list containing the names of your 5 favorite fruits.
list_5FavFruits = ["apple", "banana", "orange", "grapes", "pineapple"]

# Step 2:
# Assign this list to a variable called word_list.
word_list = list_5FavFruits

# Step 3:
#Print out the newly created list to the standard output (screen).
print(word_list)

# Step 1:
# Go to the first line of your file.

# Step 2:
# Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.

# Step 3:
# Create the random.choice method and pass the word_list variable into the choice method.
random.choice(word_list)

# Step 4:
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Step 1:
# Using the input function, ask the user to enter a single letter.
# Integrated below in Step 2

# Step 2:
# Assign the input to a variable called guess.
guess = input("Enter a single letter: ")

# Step 1:
# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

# Step 2:
# In the body of the if statement, print a message that says "Good guess!".
# Done above

# Step 3:
# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

# Step 5:
# Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print(word)