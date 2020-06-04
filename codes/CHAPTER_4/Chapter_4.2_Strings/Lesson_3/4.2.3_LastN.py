#Write a function called "last_n" that accepts two arguments:
#a string search_string and an integer n. The function should
#return the last n characters from search_string. If
#search_string is shorter than n characters, then it should
#return the entire value of search_string.


#Write your function here!
def last_n(search_string, an_integer):
    len_string = len(search_string)
    if len_string <= an_integer:
        return search_string
    return search_string[len_string-an_integer:]
    
        


#The code below will test your function. If your function
#works correctly, this should print 789, saur, and 1.
print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))




