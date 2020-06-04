#Write a function called sum_evens. sum_evens should take
#two parameters: a minimum and a maximum. It should add up
#all the even numbers between minimum and maximum and
#return the sum.
#
#sum_evens should work inclusively: both the minimum and
#the maximum should be added if they are even. For example,
#sum_evens(2, 6) -> 12 (2 + 4 + 6 = 12)


#Add your function here!
def sum_evens(minimum, maximum):
    total_sum = 0
    for i in range(minimum, maximum+1):
        if i%2 == 0:
            total_sum += i
            
    return total_sum


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 12, 0, 66, each on their own line.
print(sum_evens(2, 6))
print(sum_evens(-2, 2))
print(sum_evens(5, 17))



