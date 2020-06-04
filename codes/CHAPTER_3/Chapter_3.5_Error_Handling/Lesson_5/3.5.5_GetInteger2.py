#This exercise is identical to the previous exercise,
#except that instead of printing "Cannot convert!" when my_var
#cannot be converted to an integer, you should instead return
#the error message that results. For a reminder of how to
#access the error message in the except block, check out
#3.5.3, specifically CatchingASpecificError-4.py from 3.5.3.3
#and CatchingMultipleSpecificErrors-5.py from 3.5.3.4.
#
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return the error message that results from
#attempting to do so.
#
#Do not use any conditionals or the type() function.


#Write your function here!
def get_integer(my_var):
    try:
        number = int(my_var)
    except Exception as error:
        return error
    else:
        return number


#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#invalid literal for int() with base 10: 'Boggle.'
#5
print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))


