# Dylinh, Teresa, Sydney
# January 13, 2020
# hangman_project.py 
# Starts a game of Hangman. 

# We are going to be using the random, string and system modules.
#The random module is being used for generating a random fruit inside our list using .randchoice().
import random
# Using the string module we can easily refer to the lowercase alphabet, using string.ascii_lowercase. 
import sys
# Finally, the system module is used to exit the program anytime when inputting a '.', using sys.exit().
import string

# The program will be separated into multiple functions that will be noted below to decrease redundancy and error.
# The function wood() will print an empty gallow.
def wood():
  print("I", "-"*5, "┓", sep = '')
  for i in range(0, 3):
    print("|", sep = "" )
  print("L")

# The function body(fails), will print the text art of a gallow with new body parts appearing each time the user fails to input a correct letter. It will take the number of fails as a parameter in order to check how many body parts the hangman has before the game ends.
def body(fails):
  if (fails == 1):
    print("I", "-"*5, "┓", sep = "")
    print("|"," "*5, "O", sep = "")
    for i in range(0, 2):
      print("|", sep = "")
    print("L")

  elif (fails == 2):
    print("I", "-"*5, "┓", sep = "")
    print("|"," "*5, "O", sep = "")
    print("|"," "*5, "|", sep = "")
    print("|", sep = "")
    print("L")

  elif (fails == 3):
    print("I", "-"*5, "┓", sep = '')
    print("|"," "*5, "O", sep='' )
    print("|"," "*4, "/", "|", sep='' )
    print("|", sep ='' )
    print("L")

  elif (fails == 4):
    print("I", "-"*5, "┓", sep = "")
    print("|", " "*5, "O", sep = "")
    print("|"," "*4, "/", "|", "\ ", sep = "")
    print("|", sep = "")
    print("L")

  elif (fails == 5):
    print("I", "-"*5, "┓", sep = "")
    print("|"," "*5, "O", sep = "")
    print("|"," "*4, "/", "|", "\ ", sep = "")
    print("|"," "*5, "/", sep = "")
    print("L")

  else:
    print("I", "-"*5, "┓", sep = "")
    print("|"," "*5, "O", sep = "")
    print("|"," "*4, "/", "|", "\ ", sep = "")
    print("|"," "*4, " /","\ ", sep = "")
    print("L")

# The new_list() function will be defined to return the amount of blank spaces for the generated word. 
def new_list():
  # The length of the word is found by using the built in length function.
  length_word = len(word)
  # The list for the amount of spaces is initialized.
  space_list = []
  # Then we are using a for loop to append the amount of underscores for the word, with the list then  being returned.
  for i in range (length_word):
    space_list.append("_")
  return space_list
    
# The function fruit(), will contain all of the fruits in a list, hints for each fruit in a separate list, then it will return the random fruit and hint using the same pairing indices.
def fruit():
  fruits = ["orange", "pear", "mango", "peach", "grape", "plum", "lemon", "lime", "melon", "apricot"]

  hints = ["Rhymes with door hinge!", "It's like an apple, but not. It's often green!", "It's a tropical yellow fruit.", "It's a fuzzy fruit!", "A green ___ is sour, but a red ____ is sweeter. Known for also being purple!", "The dried fruit is called a prune.", "The duck waddled up to the ____ade stand.", "Green and sour! Superior green skittle flavour.", "I love water____!", "This fruit has a pit! It's often mistaken for a peach."]
  # Use the random module to generate a random fruit.
  generated_fruit = random.choice(fruits)
  # Find the index of the word, to find the corresponding hint.
  word_index = fruits.index(generated_fruit) 
  fruit_hint = hints[word_index]
  # Return the fruit and hint together.
  return generated_fruit, fruit_hint

# The function game() will contain the main game. 
def game():
  # Start by assigning a new variable, called letters_list for a list by calling the new_list() function for the generated fruit. We use this list to change the elements if the letters are guessed correctly by the user.
  letters_list = new_list()
  print("Guess the letters of the fruit:")
  # Output the designated blanks with no brackets.
  print("  ".join(letters_list)) 
  # Output a message on how to recieve a hint, and how to exit.
  print("\nTo quit type '.'")
  print("For a hint type '+'")
  # Initialize the fruit as a list, with each letter being their own element. 
  answer = list(word)
  # Print the gallow by calling on the wood() function.
  wood()

  # A counter of the fails will be initialized. A while loop will be made for while the fails are less than six.        
  fails = 0
  while (fails < 6):
     # Ask the user to guess the word. 
    guess = input("\nEnter your guess for a single letter: ")
    # If the user enters a "." a "Bye" message will be printed and the program will end using the system module.
    if (guess == "."):
      print("Bye!")
      sys.exit()
    # If the user enters a "+", the hint for the word will be printed.
    elif (guess == "+"):
      print(hint)
    # If the users length is equal to 1 and the guess is in the alphabet, determine if the guess is inside the answer.
    elif (len(guess) == 1) and (guess in alphabet):
      if guess in answer:
        # If the guess is in the answer, output a message and find the index of the correct element.
        print("Correct!") 
        index_letter = answer.index(guess)
        # Then the empty underscore will be changed to the letter. Change the element into the correct guess.
        letters_list[index_letter] = guess
        # Print the updated list with no brackets.
        print("  ".join(letters_list))
        # If there are no more blanks in the list, exit the loop.
        if "_" not in letters_list:
          break
      # If the correctly entered guess is not in the word, the fail counter will increase by 1 and the body function wil be called. If the guess is not a lowercase alphabetical letter, the user will be asked to enter a guess again. Finally, function will return the amount of fails. 
      else:
        print("Uh oh! Hangman gained a body part! Try again.")
        fails += 1
        body(fails)
    else:
      print("Enter one lowercase letter from the alphabet!")
  return fails


# Main Program

# A global variable for the alphabet will initialized using ascii_lowercase from the string module. Variable again is initialized as 0.
alphabet = string.ascii_lowercase 
again = 0

# Then the fruit() function will be called to initizalize the word and the corresponding hint. 
word, hint = fruit()

# Output Welcome message.
print("Welcome to Hangman - Fruit Edition!")

# The value recieved from game() is initialized into the variable fails.
fails = game()

# After the game is finished, it lets the user know it is game over and either congratulates the user on their win or tells them of their loss. 
print("\n\nGAME OVER...")
if (fails <= 5):
  print("Congratulations, You Win!\n")
else:
  # Output a message telling user what the correct fruit was.
  print("You lose!! The answer was:", word, "\n")

# The user will then prompted to answer whether or not they'd like to play again by entering 1 for yes or 2 for no. If they enter an invalid input it continues to ask. If yes, it calls fruits again, holding the first two values in order to change the special word before running the game as normal till the user would like to stop.
while (again <= 0) or (again > 2):
  try:
    again = int(input("Want to play again? (Enter 1 for yes and 2 for no) "))
    if (again == 1):
      word, hint = fruit()
      fails = game()
      if (fails <= 5):
        print("Congratulations, You Win!\n")
      else:
        print("You lose!! The answer was:", word, "\n")
    if (again == 2):
      print("Ok. Goodbye, have a nice day!")
    else:
      print("Please enter 1 or 2!")
      again = 0
  except:
    print("Please enter 1 or 2!")