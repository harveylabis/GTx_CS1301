#Write a function called copy_pointlessly. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#copy_pointlessly should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all instances of the letter A (either capital or
#   lower case) with the at sign, @
# - Replace all instances of the letter M (either capital or
#   lower case) with the character sequence |\/|
# - Replace all instances of the letter W with the character
#   sequence \/\/
# - Replace all instances of the letter O (either capital
#   or lower case) with the numeral 0
# - Alternate the case for every remaining letter in the
#   string (hint: the_string.swapcase() returns the string
#   with the case of all letters swapped)
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# This is some text. Woo text yay!
#
#Then to_upper_copy would write this text to output_file (the
#first parameter):
#
# tHIS IS S0|\/|E TEXT. \/\/00 TEXT Y@Y!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.


#Write your function here!
def copy_pointlessly(out_filename, inp_filename):
    f_input = open(inp_filename)
    contents = f_input.readlines()
    f_input.close()
    f_output = open(out_filename, 'w')
    for element in contents:
        print(translator(element.strip()), file=f_output)
    f_output.close()

    
def translator(string):
    trans_table = string.maketrans({'A':'@', 'a':'@', 'M':'|\\/|', 'm': '|\\/|', 
                                    'W':'\\/\\/', 'w':'\\/\\/', 'O':'0', 'o':'0'})
    translated = string.translate(trans_table)
    return translated.swapcase()

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#TEST @N @, TEST @N @
#TEST @N 0, TEST @N 0
#TEST @N |\/|, TEST @N |\/|
#TEST @ \/\/, TEST @ \/\/
copy_pointlessly("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")

#print(translator("This is some text. Woo text yay"))