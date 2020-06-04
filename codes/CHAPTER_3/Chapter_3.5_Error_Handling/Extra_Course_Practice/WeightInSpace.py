#Write a function called find_weight. find_weight should
#take one positional parameter, a float that represents
#the mass of an object in kilograms. It should return the
#weight of the object.
#
#You should assume that the planet is earth and that the
#acceleration due to gravity is 9.81; however, find_weight
#should also have a keyword parameter called gravity that
#allows this value to be overriden to calculate an
#object's weight on other planets.
#
#Remember, the formula for weight is mass * gravity. If
#you find Python is making rounding errors, try reversing
#the order in which you multiply the numbers.


#Add your code here!
def find_weight(mass, gravity=9.81):
    return mass*gravity


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#88.29
#33.39
print(find_weight(9.0))
print(find_weight(9.0, gravity = 3.71))






