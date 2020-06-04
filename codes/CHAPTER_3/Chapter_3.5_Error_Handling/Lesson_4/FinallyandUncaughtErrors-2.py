myString = "This string is not a number!"
#Run the code below until an error occurs
try:    
    print("Converting myString to int...")
    print(1 / 0)
    print("String #" + 1 + ": " + myString)
    myInt = int(myString)
    print(myInt)
#If an error occurs, check if it's a ValueError
except ValueError as error: 
    print(error)
#If an error occurs, check if it's a TypeError
except TypeError as error:  
    print(error)
finally:
    print("An unknown error occurred!")
print("Done!")
