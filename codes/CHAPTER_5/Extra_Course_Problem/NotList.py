#Write a function called not_list. not_list should have two
#parameters: a list of booleans and a list of integers.
#
#The list of integers will represent indices for the list of
#booleans. not_list should switch the values of all the
#booleans located at those indices.
#
#For example:
#
# bool_list = [True, False, False]
# index_list = [0, 2]
# not_list(bool_list, index_list) -> [False, False, True]
#
#After calling not_list, the booleans at indices 0 and 2
#have been switched.
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#boolean at that index twice. For example:
#
# bool_list = [True, False, False]
# index_list = [0, 2, 2]
# not_list(bool_list, index_list) -> [False, False, False]
#
#2 is in index_list twice, so the boolean at index 2 is
#switched twice: False to True, then True back to False.
#
#Hint: Remember you can change a list in place! You don't
#need to create a new list. a_list[1] = False, for example,
#changes the item in a_list at index 1 to False.

### ---     WALA KO KASABOT SA INSTRUCITON ------ ##
#Write your function here!
def not_list(bools, index):
    if len(index) == 2:
        #print("Current list of bools:", bools)
        bools[index[0]], bools[index[1]] = bools[index[1]], bools[index[0]] 
    else:
        #print("3 indices are given...")
        for _ in range(index[2]):
            #print("Current bools", bools )
            bools[index[0]], bools[index[1]] = bools[index[1]], bools[index[0]]
    #print("After swapping: ", bools)
    return bools
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[False, False, True]
#[False, False, False]
print(not_list([True, False, False], [0, 2]))
print(not_list([True, False, False], [0, 2, 2]))



