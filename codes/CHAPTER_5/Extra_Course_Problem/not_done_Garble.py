#Write a function called garble_this. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#garble_this should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all vowels with the next vowel in order (a -> e,
#   e -> i, i -> o, o -> u.
# - Replace all consonants with the next consonant, b -> c,
#   c -> d, d -> f, etc.) Replace z with b.
# - Leave everything else in the file unchanged.
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# this is some text. woo text yay!
#
#Then garble_this would write this text to output_file (the
#first parameter):
#
# vjot ot tuni viyv. xuu viyv zez!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text. You may assume
#the input file will be all lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
#
#Hints: 
# - Remember, you can increment a letter by 1 by finding its
#   ordinal, adding one, and converting it back to a letter.
#   If a_char is a character, then chr(ord(a_char) + 1) would
#   give you the next character.
# - You might also use dictionaries to establish what each
#   letter gets replaced by.
# - In ASCII, the character that comes after "z" is "{". You
#   want to replace "z" with "a", though.
# - Consider writing multiple functions! You could (but you
#   do not have to) write a dedicated function called
#   change_letter that handles a single letter, then
#   repeatedly call it to handle the file as a whole.


#Write your function here!
def garble_this(out_filename, inp_filename):
    inp_file = open(inp_filename)
    inp_contents = inp_file.readlines()
    inp_file.close()
    out_file = open(out_filename, 'w')
    for line in inp_contents:
        print(translator(line.strip()), file=out_file)
    out_file.close()   
     
        
        
def translator(phrase):
    translation_table = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'z': 'a' }
    for n in range(98, 122):
        if not chr(n) in translation_table:
            translation_table[chr(n)] = chr(n+1)
        
    translation = phrase.maketrans(translation_table)
    translated = phrase.translate(translation)
    
    return translated

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#abcdefg --> ecdfigh ecdeigh
#joklmnp
#uqrstva
#wxyzb.!
#1234567
#890&$%#

# garble_this("anOutputFile.txt", "anInputFile.txt")
# print("Done running! Check anOutputFile.txt for the result.")
