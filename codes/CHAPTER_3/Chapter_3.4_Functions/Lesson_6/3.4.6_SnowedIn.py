#Write a function called snowed_in that will determine
#whether school is closed based on the weather and
#temperature. We'll pretend the school is in Georgia, where
#a little snow or sub-freezing temperatures are enough to
#close down schools!
#
#The function should take three parameters:
#
# - temperature, a float
# - weather, a string
# - is_celsius, a boolean
#
#The function should return True if temperature is below
#freezing (32 if is_celsius is False, 0 if is_celsius is
#True) or if weather is "snowy". Otherwise, it should
#return False.
#
#Note, however, that is_celsius should be an optional
#argument. If the function call does not supply a value for
#is_celsius, assume it is True.
#
#For example:
#
# snowed_in(15, "sunny") -> False
# is_celsius is assumed to be True, so 15 is not below
# freezing.
#
# snowed_in(15, "sunny", is_celsius = False) -> True
# is_celsius is False, so 15 is below freezing.
#
# snowed_in(15, "snowy", is_celsius = True) -> True
# The weather is "snowy", so the temperature doesn't matter.


#Write your function here!
def snowed_in(temperature, weather, is_celsius=True):
    if weather == "snowy":
        return True
    elif (temperature < 0 and is_celsius) or (temperature < 32 and not is_celsius):
        return True
    else:
        return False
    
    #return weather == "snowy" or temperature < 0 and is_celsius) or (temperature < 32 and not is_celsius)
                


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print False, True, and True, each on their own line.

print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True





