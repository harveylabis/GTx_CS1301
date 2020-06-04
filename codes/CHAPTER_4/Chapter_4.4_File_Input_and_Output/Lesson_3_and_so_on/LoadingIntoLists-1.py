myList = []

#Open OutputFile.txt in read mode
inputFile = open("OutputFile.txt", "r")    

#For each line in the file
for line in inputFile:  
    #Add the line to myList, stripping out whitespace
    myList.append(line.strip()) 

print(myList)

inputFile.close()


