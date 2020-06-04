#Checks if searchString is not in checkString
def checkNotInString(checkString, searchString): 
    if searchString not in checkString:
        print(searchString + " was not found!")
    else:
        print(searchString + " was found!")

myString = "ABCDE"
checkNotInString(myString, "BC")
checkNotInString(myString, "GH")
