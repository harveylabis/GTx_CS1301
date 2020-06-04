input_string = "12sdsd3.4"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine that you're writing some software for a check-out
#register. The software tries to guess what information was
#entered based on its structure:
#
# - If the information entered as all numbers, then it's a
#   PIN number.
# - If the information entered was a number with a decimal,
#   it's a transaction amount.
# - If the information entered was neither, it's a password.
#
#Write some code to figure out which of these types of
#information the inputted string is. Print "PIN" for PIN
#number, "amount" for transaction amount, or "password" for
#password. You may assume these are the only three possible
#outcomes.
#
#Hint: You can do this however you want, but error handling
#will be easier than using conditionals.


#Add your code here!
def isInt(given_int):
    try:
        given_int = int(given_int)
    except:
        return False
    else:
        return True
    
def isFloat(given_float):
    try:
       given_float = float(given_float)
    except:
        return False
    else:
        return True
    
    
def figureOut(info_entered):
    if isInt(info_entered):
        print("PIN")
    elif isFloat(info_entered):
        print("amount")
    else:
        print("password")
        
    return None
    
figureOut(input_string)    
    






