#Write a function called check_date. check_date should
#require two positional parameters: a string representing
#the name of a month, and an integer representing a date.
#check_date should also have a keyword parameter called
#is_leap_year, assumed to be False, representing whether or
#not it's a leap year.
#
#Return True if the date is a valid calendar date. Return
#False if it is not. A date may not be a valid calendar
#date if the month isn't a real month, or if that date does
#not exist for that month. You can see some examples at the
#end of this file.
#
#Remember: 30 days has September, April, June, and November.
#All the rest have 31, except February, which has 28, until
#Leap Year gives it 29.
#
#You may assume that day will be greater than 0 (you don't
#need to check negative or zero values for day).


#Write your function here!
def check_date(month, date, is_leap_year=False):
    days_equals_30 = ['September', 'April', 'June', 'November']
    days_equals_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    
    if month in days_equals_30 and 1 <= date <= 30:
        return True
    elif month in days_equals_31 and 1 <= date <= 31:
        return True
    elif is_leap_year and month.title() == 'February' and 1 <= date <= 29:
        return True
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line.
print(check_date("January", 31))
print(check_date("February", 29, is_leap_year = True))
print(check_date("Techtember", 15, is_leap_year = True))
print(check_date("June", 31))




