import random
#Get a random number from 1 to 100
hiddenNumber = random.randint(1, 100)
#Create userGuess and give is a value that can't be correct
userGuess = 0   
#Repeat until the guess is correct
while not userGuess == hiddenNumber:    
    #Get the user's next guess as an integer
    userGuess = int(input("Guess a number: "))  
    #Check if the guess is too high
    if userGuess > hiddenNumber:    
        print("Too high!")
    #Check if the guess is too low
    elif userGuess < hiddenNumber:  
        print("Too low!")
    #The guess must be right!
    else:   
        print("That's right!")


