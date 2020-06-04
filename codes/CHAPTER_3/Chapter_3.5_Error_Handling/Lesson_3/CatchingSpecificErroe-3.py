myString = "This string is not a number!"
#Run the code below until an error occurs
try:    
    print("Converting myString to int...")
    myInt = int(myString)
    print(myInt)
#If a ValueError occurs, jump to here
except ValueError as error: 
    print(error)
print("Done!")
