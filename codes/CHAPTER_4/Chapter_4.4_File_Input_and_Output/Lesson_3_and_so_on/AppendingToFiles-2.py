myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in append mode
outputFile = open("OutputFile.txt", "a")

#For each name in myList
for name in myList:
    #Write the name to the file on its own line
    print(name, file = outputFile)

outputFile.close()


