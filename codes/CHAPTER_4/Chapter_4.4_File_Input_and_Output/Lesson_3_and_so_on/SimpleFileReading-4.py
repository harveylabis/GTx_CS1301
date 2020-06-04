inputFile = open("OutputFile.txt", "r")

#Read the next line of inputFile, cast it 
#to int, and assign it to myInt1
myInt1 = int(inputFile.readline())  
#Read the next line of inputFile, cast it 
#to int, and assign it to myInt2
myInt2 = int(inputFile.readline())  
#Read the next line of inputFile, cast it 
#to int, and assign it to myInt3
myInt3 = int(inputFile.readline())  

print("myInt1:", myInt1)
print("myInt2:", myInt2)
print("myInt3:", myInt3)

inputFile.close()


