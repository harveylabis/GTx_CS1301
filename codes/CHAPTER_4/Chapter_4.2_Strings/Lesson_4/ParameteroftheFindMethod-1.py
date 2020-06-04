myString = "ABCDEABCDEABCDE"

#Prints the first index of "CDE" in myString
print(myString.find("CDE")) 
#Prints the first index of "CDE" in myString after 5
print(myString.find("CDE", 5)) 
#Prints the first index of "CDE" in myString after 8
print(myString.find("CDE", 13)) 
#Prints the first index of "CDE" in myString between 4 and 10
print(myString.find("CDE", 4, 10)) 
#Prints the first index of "CDE" in myString between 3 and 6
print(myString.find("CDE", 3, 6)) 
