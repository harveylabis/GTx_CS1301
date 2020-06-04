#Write a function called find_weight. find_weight should
#take one parameter, a float that represents the mass of
#an object in kilograms. It should return the weight of
#the object on earth.
#
#Remember, the formula for weight is mass * gravity. You
#should use 9.81 as the value for gravity on earth. If
#you find Python is making rounding errors, try reversing
#the order in which you multiply the numbers.


#Add your code here!
def find_weight(mass):
    return mass * 9.81


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#88.29
#11.772
print(find_weight(9.0))
print(find_weight(1.2))






