myList = []

#Open OutputFile.txt in read mode
inputFile = open("OutputFile.txt", "r")    

myInt1 = int(inputFile.readline())  
myInt2 = int(inputFile.readline())  
myInt3 = int(inputFile.readline())  
#For each line in the file
for line in inputFile:  
    #Add the line to myList, stripping out whitespace
    myList.append(line.strip()) 

print(myInt1)
print(myInt2)
print(myInt3)
print(myList)

inputFile.close()


