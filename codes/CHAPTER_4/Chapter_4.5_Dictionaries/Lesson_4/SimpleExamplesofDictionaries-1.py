myString = "This is the string whose words we would like to count. This string contains some repeated words, as well as some unique words. It contains punctuation, and it contains words that are capitalized in different ways. If the method we write runs correctly, it will count 4 instances of the word 'it', 3 instances of the word 'this', and 3 instances of the word 'count'."

myString = myString.replace(".","") #Remove periods
myString = myString.replace(",","") #Remove commas
myString = myString.replace("'","") #Remove apostrophes
myString = myString.lower() #Make all lower case
mySplitString = myString.split() #Split by spaces

wordDictionary = {} #Create empty dictionary
for word in mySplitString:  #For each word in the split string
    if word in wordDictionary:  #If it's already been found...
        wordDictionary[word] += 1   #Add one to its count
    else:   #Otherwise...
        wordDictionary[word] = 1 #Create it with value 1

print(wordDictionary)


