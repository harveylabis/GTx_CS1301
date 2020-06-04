mystery_value = 9

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and 
#prints the result. In the case that mystery_value is 
#equal to 0, print "Can't divide by zero". If for any other
#reason the operation fails, print "Not possible".
#
#You may not use any conditionals or the type() function.


#Add your code here!
try:
    print(10/mystery_value)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Not possible")
    



