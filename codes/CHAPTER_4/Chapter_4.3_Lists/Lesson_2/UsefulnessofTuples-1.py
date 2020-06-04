#Returns a tuple containing the quotient and remainder
def quotientAndRemainder(dividend, divisor):    
    #Gets the quotient
    quotient = dividend // divisor  
    #Gets the remainder
    remainder = dividend % divisor  
    #Returns the tuple of the quotient and remainder
    return (quotient, remainder)    

myDividend = 11
myDivisor = 4
tupleResults = quotientAndRemainder(myDividend, myDivisor)

#Prints the first element of tupleResults
print("Quotient:", tupleResults[0])
#Prints the second element of tupleResults
print("Remainder:", tupleResults[1])


