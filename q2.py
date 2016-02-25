#Lam Le
# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4,
# then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.

import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():
    # TODO: write code in this functiont that:
    # 1. Asks the user to enter their input (between 1 and 4)
    # 2. Checks that the user's input is valid. If it's not valid (if it's not between 1 and 4), then ask the user to re-enter their input.
    # 3. Once the user enters a valid input, return that input as an integer.
    print('How many sticks would you like to pick up? Choose between 1 and 4') #Asks user how many sticks they would like to pick up
    userChoice = input() #Users choice 
    if userChoice in range(1,4): #If the users choice is between 1 and 4. Continue.
        return userChoice #Returns the users choice
    else: #Else statement saying that if you choose a number outside of 1 and 4. It is invalid.
        print('sorry your choice is invalid. Please re-enter your input.') #Telling the user that your input is invalid.
    
def subtractSticks( number ):
    
    global sticks 
    # TODO: write code inside this function that:
    # 1. subtracts the parameter `number` from the global variable `sticks`
    # 2. checks if the number subtracted resulted in the last stick, if so, return True
    # 3. if there are still sticks left, return False
    sticks = sticks - number #subtracts the number from the variable sticks
    if sticks <=0: #if statement stating if the number subtracted resulted in the last trick, its True 
        return True 
    else: #else statement stating if there are sticks left, its False
        return False
 
    
def determineComputerChoice():
    # TODO: write code inside this function that returns an integer between 1 and 4, random chosen by the computer
    computerChoice = random.randint(1,4) #returns a random integer between 1 and 4 chosen by the computer
    return computerChoice
