myInt1 = 12
myInt2 = 23
myInt3 = 34
myList = ["David", "Lucy", "Vrushali", "Ping", 
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")    

#Write myInt1 to outputFile
outputFile.write(str(myInt1) + "\n")    
#Write myInt2 to outputFile
outputFile.write(str(myInt2) + "\n")    
#Write myInt3 to outputFile
outputFile.write(str(myInt3) + "\n")    
#Joins myList using \n, then writes it to a file
outputFile.write("\n".join(myList))   

outputFile.close()


