try:
    #Open InputFile.txt in read-only mode
    inputFile = open("InputFile.txt", mode = "r")  
    try:
        #For each line in the file
        for line in inputFile:  
            #Print the line
            print(int(line)) 
    #Catch a ValueError
    except ValueError as error:    
        print("A value error occurred!")
    else:
        print("No errors occurred converting the file!")
    finally:
        #Close the file
        inputFile.close()  
#Catch an IOError
except IOError as error:
    print("An error occurred reading the file!")
