#Get the number of numbers to average
numCount = int(input("How many numbers will you average? "))   
#Loop numCount times
for i in range(1, numCount + 1):  
    #Creates sum with the value 0
    sum = 0 
    #Gets the user's number
    nextNumber = int(input("Enter number #" + str(i) + ": "))   
    #Add the inputted number to the sum
    sum += nextNumber 
#Print the sum over numCount
print(sum / numCount)   


