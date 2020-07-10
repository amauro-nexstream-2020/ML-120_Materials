import random
import sys

# We will be using the following encoding for rock, paper, scissors, lizard, and Spock:
#   Rock     = 0
#   Paper    = 1
#   Scissors = 2
#   Lizard   = 3
#   Spock    = 4
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
  # TODO: finish this if statement

      
  elif(userInput == 1):
    if(computerInput == 0):
      print("Paper beats rock! You win!")
    elif(computerInput == 1):
      print("Paper against paper! It's a tie!")
    elif(computerInput == 2):
      print("Scissors beats paper! You lose!")
  # TODO: finish this if statement


  elif(userInput == 2):
    if(computerInput == 0):
      print("Rock beats scissors! You lose!")
    elif(computerInput == 1):
      print("Scissors beats paper! You win!")
    elif(computerInput == 2):
      print("Scissors against scissors! You win!")
  # TODO: finish this if statement

#TODO: add cases for userInput == 3, 4
    




#The main part of our program. Everything below here will run when we press the play button.
playing = True

while(playing):
# Step 1: Get the user input
  userInput = int(input("\nEnter rock (0), paper (1), scissors (2), lizard (3), or Spock(4)\n"))

# Step 2: Making sure that the user inputted a correct value
  if(userInput < 0 or userInput > 4):
    print("Please input 0, 1, or 2.")
    continue

# Step 3: TODO: Finish the statement below, using a method from Python's random API. computerInput should be between 0 and 2.
  computerInput = random.randint(0, 4)

# Step 4: Printing out the computer's choice of rock, paper, or scissors
  if(computerInput == 0):
    print("Computer chose rock.")
  elif(computerInput == 1):
    print("Computer chose paper.")
  elif(computerInput == 2):
    print("Computer chose scissors.")
  elif(computerInput == 3):
    print("Computer chose lizard.")
  elif(computerInput == 4):
    print("Computer chose Spock.")
  else:
    print("Invalid input from computer: " + computerInput)
    continue

# Step 5: Calling the determineWinner method here
  determineWinner(userInput, computerInput)

# Step 6: Seeing if the user would like to play the game again
  playAgain = input("\nPlay again? [y or n]\n")
  if(playAgain == "n"):
    playing = False
