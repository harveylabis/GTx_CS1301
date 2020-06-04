from datetime import date

#First, we know we want a function called get_todays_date.
#So, let's create it:

def get_todays_date():
    #Next, we know we need to actually access today's date
    #to be able to print it. The comments in the directions
    #tell us how: date.today()
    
    todays_date = date.today()
    
    #By default, str(todays_date) doesn't give us the format
    #we want. So, we need to create our result manually.
    #
    #We could do this in one long line, but let's break it
    #up. First, let's just create the empty string that we
    #will eventually return:
    
    date_string = ""
    
    #Now, let's add each piece that we need to it one by one.
    #Remember, to add an integer to a string, we first need
    #to convert it to a string using str(). It might have
    #been a while since you've done that since until now,
    #you've been mostly printing integers directly.
    
    date_string += str(todays_date.year)
    date_string += "/"
    date_string += str(todays_date.month)
    date_string += "/"
    date_string += str(todays_date.day)
    
    #Now, date_string has the value we wanted to return. So,
    #we return it:
    
    return date_string

#Now, outside the function, we'll find that if we call the
#function, it will print the right output:
print(get_todays_date())





