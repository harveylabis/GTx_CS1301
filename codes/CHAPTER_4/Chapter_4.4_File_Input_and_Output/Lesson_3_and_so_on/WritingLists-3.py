myList = ["David", "Lucy", "Vrushali", "Ping",
          "Natalie", "Dana", "Addison", "Jasmine"]
 
#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")    
 
#Joins myList using \n, then writes it to a file
outputFile.write("\n".join(myList))   
 
outputFile.close()
