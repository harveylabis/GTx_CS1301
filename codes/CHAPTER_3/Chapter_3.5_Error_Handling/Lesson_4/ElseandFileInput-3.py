try:
    #Open InputFile.txt in read-only mode
    inputFile = open("FakeInputFile.txt", mode = "r")  
#Catch an IOError
except IOError as error:    
    print("An input error occurred!")
else:
    #For each line in the file
    for line in inputFile:  
        #Print the line
        print(line) 
    #Close the file
    inputFile.close()   
