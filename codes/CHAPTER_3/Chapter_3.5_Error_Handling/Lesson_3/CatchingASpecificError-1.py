myString = "This string is not a number!"
#Run the code below until an error occurs
try:    
    print("Converting myString to int...")
    print("String #" + 1 + ": " + myString)
    myInt = int(myString)
    print(myInt)
#If an error occurs, jump to here
except: 
    print("Can't convert; myString not a number.")
print("Done!")
