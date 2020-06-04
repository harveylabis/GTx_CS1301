#Write a function called is_palindrome. The function should
#have one parameter, a string. The function should return
#True if the string is a palindrome, False if not.
#
#A palindrome is a sequence of letters that is the same
#forward and backward. For example, "racecar" is a
#palindrome. In determining whether a string is a palindrome
#or not, you should ignore punctuation, capitalization and
#spaces. For example, "Madam in Eden, I'm Adam" is a
#palindrome.
#
#You may assume that the only characters in the string will
#be letters, spaces, apostrophes, commas, periods, and
#question marks.
#
#Hint: Before checking if the string is a palindrome, get
#rid of the spaces and punctuation marks using the replace()
#method and convert the entire string to upper or lower
#case using the upper() or lower() methods.
#
#Hint 2: There are multiple ways to do this! If you're stuck
#on one way, try a different one. You could use string
#slicing, a for loop, or some string methods. Or, try
#printing the string at different stages to see what's going
#wrong!


#Write your function here!
def is_palindrome(phrase):
    phrase = string_cleaner(phrase)
    return phrase[::-1] == phrase
        
def string_cleaner(string):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ " "'
    for element in string:
        if element in punctuation:
            string = string.replace(element, '')
            
    return string.lower()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, each on their own line.
print(is_palindrome("racecar"))
print(is_palindrome("Madam in Eden, I'm Adam"))
print(is_palindrome("Mister in Eden, I'm Eve"))



