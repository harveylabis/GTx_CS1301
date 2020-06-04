try:
    #Open NumberAndLetterFile.txt in read-only mode
    inputFile = open("NumberAndLetterFile.txt", mode = "r")  
    #For each line in the file
    for line in inputFile:  
        try:
            #Print the line
            print(int(line)) 
        #Catch a ValueError
        except ValueError as error:    
            print("A value error occurred!")
        else:
            print("No errors occurred converting this line!")
    #Close the file
    inputFile.close()   
#Catch an IOError
except IOError as error:
    print("An error occurred reading the file!")
