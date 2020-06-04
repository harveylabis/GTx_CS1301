#Write a function called remainder. remainder should take
#two parameters: a dividend and a divisor. It should return
#the remainder when you divide the dividend by the divisor.
#
#For example:
# remainder(9, 3) -> 0
# remainder(8, 3) -> 2
# remainder(7, 3) -> 1
# remainder(6, 3) -> 0
#
#You may not use Python's built-in modulus operator. The
#symbol for that operator should not appear anywhere in your
#code.
#
#You may assume both dividend and divisor will be greater
#than 0


#Add your function here!
def remainder(dividend, divisor):
    whole_num_qoutient = dividend//divisor
    remainder_difference = dividend - (whole_num_qoutient * divisor)
    
    return remainder_difference
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 0, 3, 2
print(remainder(9, 3))
print(remainder(11, 4))
print(remainder(27, 5))



