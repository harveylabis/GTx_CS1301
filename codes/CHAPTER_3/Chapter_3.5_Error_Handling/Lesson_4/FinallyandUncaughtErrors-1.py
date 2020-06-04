#Open InputFile.txt in read-only mode
inputFile = open("NumberFile.txt", mode = "r")  
try:
    #For each line in the file
    for line in inputFile:  
        #Print the line
        print(int(line)) 
#Catch an IOError
except ValueError as error:    
    print("A value error occurred!")
else:
    print("No errors occurred!")
#Close the file
inputFile.close()   
