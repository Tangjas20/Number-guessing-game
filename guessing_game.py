"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def start_game():
  usedNumbersList = [-1] #This is the list that records all randInt's
  playAgain = True #Initialises variable to be used later on
  randInt = -1 #Intialises the variable to be used later on so I don't get a unassigned variable error
  highscore = 999 #Initialises variable.
  
  while playAgain == True: 
    #When the program starts, we want to:
    #------------------------------------
    #1. Display an intro/welcome message to the player.
    print("############")
    print("#~Welcome!~#")
    print("#~~To The~~#")
    print("#~~Number~~#")
    print("#~~~Game~~~#")
    print("############")
    
    if highscore == 999:
      print("There is no highscore yet!")
    else:
      print("The high score is {}. Can you beat it?".format(highscore))
    
    #2. Store a random number as the answer/solution.
    while randInt in usedNumbersList:
      randInt = random.randint(1,10)

    #This ensures that different numbers are used.
    usedNumbersList.append(randInt)
    
    #3. Continuously prompt the player for a guess
    playerGuessInt = 0
    guessCounter = 0
    
    while playerGuessInt != randInt:
      guessCounter += 1
      validInput = False

      while validInput == False:
        playerGuessInt = input("What is your guess between 1-10? ")

        try:
          playerGuessInt = int(playerGuessInt)

        #a.If the guess greater than the solution, display to the player "It's lower"
          if playerGuessInt > 10 or playerGuessInt < 1: #Keeps the guesses between 1-10
            print("Keep it between 1-10 please!")
            validInput = False

          elif playerGuessInt > randInt: #Control flow is used, if the IF statements order are changed 
  #                                          it would have different outcomes
            print("It's lower")
            validInput = True

        #b If the guess is less than the solution, display to the player "It's higher"
          elif playerGuessInt < randInt:
            print("It's higher")
            validInput = True

        #c If the guess is corret, validInput 
          elif playerGuessInt == randInt:
            validInput = True

        #d If the input is not an integer it will lead to the exception block
        except:
            print("Please input a valid integer!")
            validInput = False


          
    #4. Once the guess is correct, stop looping, inform the user they "Got it"
    print("Got it!")
    #and show how many attempts it took them to get the correct number
    print("It took {} attempts to get the correct number {}. Good job!".format(guessCounter,randInt))
    
    if guessCounter <= highscore:
      highscore = guessCounter
    
    playAgainInput = input("Would you like to play again? Y/N ")

    #Sets the loop to stop if anything but a 'y' is inputted
    if playAgainInput.lower() != 'y':
      playAgain = False
    #5. Let the player know the game is ending, or something that indicates the game is over
      print("############")
      print("#~~Thanks~~#")
      print("#~~~~For~~~#")
      print("#~playing!~#")
      print("#~~~Cya!~~~#")
      print("############")

    
    

# Kick off the program by calling the start_game function.
start_game()
