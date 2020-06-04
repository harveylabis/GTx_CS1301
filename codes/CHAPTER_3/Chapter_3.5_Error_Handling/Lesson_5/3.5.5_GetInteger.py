#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return a message that says, "Cannot convert!"
#
#For example, for "5" as the value of my_var, get_integer would
#return the integer 5. If the value of my_var is the string
#"Boggle.", then get_integer would return a string with the
#value "Cannot convert!"
#
#Do not use any conditionals or the type() function.


#Write your function here!
def get_integer(number):
    try:
        my_var = int(number)
    except Exception:
        return "Cannot convert!"
    else:
        return my_var



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))


