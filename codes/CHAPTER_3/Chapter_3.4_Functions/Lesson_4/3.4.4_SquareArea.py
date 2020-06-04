#Write a function that takes in one integer parameter, the
#side length of a square, and returns the area. The function
#should be named find_area, and have one parameter:
#side_length.


#Write your function here!
def find_area(side_length):
    return side_length**2

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))


