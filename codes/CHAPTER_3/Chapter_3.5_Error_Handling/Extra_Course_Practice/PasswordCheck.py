#Write a function called password_check. password_check should
#take as input a single string. It should return a boolean:
#True if the password is a valid password according to the rules
#below, False if it is not.
#
#A string is a valid password if it meets ALL the following
#conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   numbers, and punctuation. For punctuation, the following
#   punctuation marks are acceptable: !@#$%&()-_[]{};':",./<>?
# - It may not contain any characters that do not fit into the
#   four categories above. This includes any punctuation marks
#   not listed in the bullet point above, spaces, and any other
#   character.


#Add your code here!
def password_check(password):
    if len(password) > 7 and valid_char(password):
        return True
    else:
        return False
        

def valid_char(string):
    # starting values
    upper = False
    lower = False
    number = False
    punc = False
    any_other_char = False
    # punctuations 
    punctuations = '!@#$%&()-_[]{};\':\",./<>?'
    # checking each letter properties
    for letter in string:
        ord_letter = ord(letter)
        if 65 <= ord_letter <= 90:
            upper = True    # present uppercase
        elif 97 <= ord_letter <= 122:
            lower = True    # present lowercase
        elif 48 <= ord_letter <= 57:
            number = True    # present number
        elif letter in punctuations:
            punc = True        # present punctuation
        else:
            any_other_char = True    # char shouldn't be included
        # return True once all have representative
        if upper and lower and number and punc and not any_other_char:
            return True
        
    return False
            
        
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(password_check("tHIs1sag00d.p4ssw0rd."))
print(password_check("3@t7ENZ((T"))
print(password_check("2.shOrt"))
print(password_check("all.l0wer.case"))
print(password_check("inv4l1d CH4R4CTERS~"))



