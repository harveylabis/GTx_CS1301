mystery_value = 9

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that mystery_value is equal to 0,
#print "Not possible". Do not catch any other errors. This
#means there will be an uncaught error in the correct answer!
#
#You may not use any conditionals or the type() function.


#Add your code here!
try:
    print(10/mystery_value)
except ZeroDivisionError:
    print("Not possible")
    

