mystery_value = "9"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that an error occurs, print "Not
#possible".
#
#Use error handling to determine if an error will occur; do
#not use the type() function. You might be surprised how many
#types Python can divide by 10!


#Add your code here!


try:
    my_new_num = 10 / mystery_value
    print(my_new_num)
except:
    print("Not possible")