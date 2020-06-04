#We've written the function, reverse, below. This function
#takes a string and returns the reverse of it. There are two
#scope errors somewhere in the code. Read through all the
#code below to find and fix the errors, so that the function
#produces the correct output and the result of the function
#is correctly printed. Note that you should not change the
#three lines that are already present in the function, but
#you may add lines before them, or you may change or add to
#the lines outside the function.
#
#Note that your goal here is to fix both the function itself
#and the program as a whole. So, your function should be
#able to be called on a new string, and the program when
#run should print the reverse of the string originally on
#line 29.


def reverse(a_string):
    #You may add code before the following three lines.
    
    rev = ''
    
    #Don't change these three lines.
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]
    return rev


#You may change or add to the following lines.
result = reverse("This string should be reversed!")
print(result)




