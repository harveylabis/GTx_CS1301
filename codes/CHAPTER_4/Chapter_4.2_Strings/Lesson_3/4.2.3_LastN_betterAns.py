#There are a lot of complicated approaches we could take
#here, but the simplest is just a string slicing operation.
#If we want to start n characters from the end, then we grab
#a slice that starts at -n and goes until the end.

def last_n(search_string, n):
    return search_string[-n:]

#We also don't need any special reasoning to handle instances
#where search_string is shorter than n characters; by
#default, Python just grabs the entire string if that is the
#case.


print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))




