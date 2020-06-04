#Saves inList to the file
def save(filename, inList): 
    outputFile = open(filename, "w")

    for item in inList: 
        print(item, file = outputFile)   

    outputFile.close()

#Loads from filename and returns a list of the contents
def load(filename): 
    inputFile = open(filename, "r")
    inList = []

    for line in inputFile:
        inList.append(line.strip())
    inputFile.close()
    return inList

myList = ["David", "Lucy", "Vrushali", "Ping", "Natalie",
          "Dana", "Addison", "Jasmine"]
save("OutputFile.txt", myList)
newList = load("OutputFile.txt")

print(newList)


