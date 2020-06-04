#Helping us develop this class are a team of teaching
#assistants, often called TAs for short.
#
#Write a function called my_TAs. The function should take as
#input three strings: first_TA, second_TA, and third_TA. It
#should return as output the string, "[first_TA], [second_TA],
#and [third_TA] are awesome!", with the values replacing the
#variable names.
#
#For example, my_TAs("Sridevi", "Lucy", "Xu") would return
#the string "Sridevi, Lucy, and Xu are awesome!"
#
#Hint: Notice that because you're returning a string instead
#of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
#it!


#Write your function here!
def my_TAs(TA_1, TA_2, TA_3):
    return "{}, {}, and {} are awesome!".format(TA_1, TA_2, TA_3)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Joshua, Jackie, and Marguerite are awesome!".
test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))






