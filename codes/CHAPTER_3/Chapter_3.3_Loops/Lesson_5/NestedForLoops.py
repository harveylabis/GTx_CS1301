#Creates listOfStrings and assigns it a list of strings each with 
#multiple words
listOfStrings = ["This is the first string", "This is the second string",
                 "This is the third string", "This is the fourth string",
                 "This is the fifth string"]
numSpaces = 0
#Loops over each string in listOfStrings
for currentString in listOfStrings: 
    #Loops over each character in currentString
    for currentCharacter in currentString:  
        #Checks if the current character is a space
        if currentCharacter == " ": 
            numSpaces += 1

numWords = numSpaces + len(listOfStrings)  
print("There are", numWords, "words in these strings.")


