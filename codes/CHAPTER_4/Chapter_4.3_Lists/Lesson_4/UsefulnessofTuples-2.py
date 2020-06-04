#Returns a tuple containing the quotient and remainder
def quotientAndRemainder(dividend, divisor):    
    #Returns the tuple of the quotient and remainder
    return (dividend // divisor, dividend % divisor)    

myDividend = 11
myDivisor = 4
#Assigns the first value of the result to myQuotient and 
#the second to myRemainder
(myQuotient, myRemainder) = quotientAndRemainder(myDividend, myDivisor)

print("Quotient:", myQuotient)
print("Remainder:", myRemainder)


