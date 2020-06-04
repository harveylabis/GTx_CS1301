myString = "1"
#Run the code below until an error occurs
try:    
    print("Converting myString to int...")
    myInt = int(myString)
    print(myInt)
#If an error occurs, check if it's a ValueError or 
#TypeError
except (ValueError, TypeError) as error: 
    print("A ValueError or TypeError occurred.")
#Check if some other type of error occurred
except Exception as error:  
    print("Some other type of error occurred.")
#If no errors occurred, then do the following
else:   
    print("No errors occurred!")
print("Done!")


