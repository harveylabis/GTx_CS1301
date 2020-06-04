#Write a function called delete_from_list. delete_from_list
#should have two parameters: a list of strings and a list of
#integers.
#
#The list of integers represents the indices of the items to
#delete from the list of strings. Delete the items from the
#list of strings, and return the resulting list.
#
#For example:
#
# delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5])
#
#...would return the list ["c", "d"]. "a" is at index 0, "b" at 1,
#"e" at 4, and "f" at 5, so they would all be removed.
#
#Remember, though, as you delete items from the list, the
#indices of the remaining items will change. For example, once
#you delete "a" at index 0, the list will be ["b", "c", "d",
#"e", "f"], and now "c" will be at index 1 instead of "b". The
#list of indices to delete gives those values' _original_
#positions.
#
#You may assume that there are no duplicate items in the list
#of strings.
#
#There is more than one way to do this, so if you find yourself
#struggling with one way, try a different one!


#Write your function here!
def delete_from_list(string_list, indices):
    for i in indices:
        string_list[i] = None
    
    return [x for x in string_list if x != None]

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#['c', 'd']
#['a', 'b', 'e', 'f']
print(delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5]))
print(delete_from_list(["a", "b", "c", "d", "e", "f"], [2, 3]))
print(delete_from_list(["Aesop", "mosquitoes", "Aldrich", "terrace", "mucus", "histamine", 
                        "extirpate", "redcoat", "waterfall"], [6, 5, 3]))

