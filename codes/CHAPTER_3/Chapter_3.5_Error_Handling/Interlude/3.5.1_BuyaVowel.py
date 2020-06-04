#Write a function called has_a_vowel. has_a_vowel should have
#one parameter, a string. It should return True if the string
#has any vowels in it, False if it does not.


def has_a_vowel(a_str):
    #print("Starting...")
    for letter in a_str:
        #print("Checking", letter)
        if letter in "aeiou":
            #print(letter, "is a vowel, returning True")
            print("Done!")
            return True
    #print(letter, "is not a vowel, returning False")
    print("Done!")
    return False
    
    
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then True, then False, then False, each on
#its own line.
print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))


