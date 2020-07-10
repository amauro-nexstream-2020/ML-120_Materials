import random
import sys

# We will be using the following encoding for rock, paper, and scissors:
#   Rock     = 0
#   Paper    = 1
#   Scissors = 2
#
# Fill in the below method with the rules of the game.
# determineWinner is a structure called a method. The code in the method will run every time it is called.
def determineWinner(userInput, computerInput):
  if(userInput == 0):   
    if(computerInput == 0):
      print("Rock against rock! It's a tie!")
    elif(computerInput == 1):
      print("Paper beats rock! You lose!")
    elif(computerInput == 2):
      print("Rock beats scissors! You win!")

# TODO: Fill in the code below using the above if statement as an example.
  elif(userInput == 1):

  elif(userInput == 2):




#The main part of our program. Everything below here will run when we press the play button.
playing = True

while(playing):
# Step 1: Get the user input
  userInput = int(input("\nEnter rock (0), paper (1), or scissors (2)\n"))

# Step 2: Making sure that the user inputted a correct value
  if(userInput != 0 and userInput != 1 and userInput != 2):
    print("Please input 0, 1, or 2.")
    continue

# Step 3: TODO: Finish the statement below, using a method from Python's random API. computerInput should be between 0 and 2.
  computerInput = random.

# Step 4: Printing out the computer's choice of rock, paper, or scissors
  if(computerInput == 0):
    print("Computer chose rock.")
  elif(computerInput == 1):
    print("Computer chose paper.")
  elif(computerInput == 2):
    print("Computer chose scissors.")
  else:
    print("Invalid input from computer: " + computerInput)
    continue

# Step 5: Calling the determineWinner method here
  determineWinner(userInput, computerInput)

# Step 6: Seeing if the user would like to play the game again
  playAgain = input("\nPlay again? [y or n]\n")
  if(playAgain == "n"):
    playing = False
