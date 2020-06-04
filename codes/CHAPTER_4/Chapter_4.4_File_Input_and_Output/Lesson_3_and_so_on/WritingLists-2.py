myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")    

#Writes every string in myList to a file
outputFile.writelines(myList)   

outputFile.close()


