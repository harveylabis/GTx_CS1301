myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")    

#For each name in myList
for name in myList: 
    #Write the name to the file on its own line
    print(name, file = outputFile)   

outputFile.close()


