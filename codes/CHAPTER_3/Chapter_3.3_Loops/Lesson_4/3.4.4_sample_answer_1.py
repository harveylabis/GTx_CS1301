mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

#The goal of this problem is to think about a while loop
#that handles multiple conditions.
#
#In this case, we care whether each of the values above is
#greater than 0. If *any* of them are, then the loop should
#continue. Since it only takes one of those conditions being
#true to continue, we're going to use 'or':

while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    
    #If the lines inside the loop are running, it means
    #that one or more of the values are greater than 0. When
    #that happens, the directions said to subtract one from
    #each of the values:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    
    #Then, to print them all on one line, we can use this
    #syntax to print them separated by spaces:
    print(mystery_int_1, mystery_int_2, mystery_int_3)

#Note that the first line could have also been written as:
# while not (mystery_int_1 <= 0 and mystery_int_2 <= 0 and mystery_int_3 <= 0):
#
#The syntax on line 13 says, "While any of these conditions
#are true." The syntax on line 28 says, "While all of these
#conditions aren't False."




