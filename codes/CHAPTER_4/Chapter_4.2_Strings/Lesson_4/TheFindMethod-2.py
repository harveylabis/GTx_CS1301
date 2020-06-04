#Checks if searchString is in checkString
def checkInString(checkString, searchString): 
    if checkString.find(searchString) >= 0:
        print(searchString + " was found!")
    else:
        print(searchString + " was not found!")

myString = "ABCDE"
checkInString(myString, "BC")
checkInString(myString, "GH")
