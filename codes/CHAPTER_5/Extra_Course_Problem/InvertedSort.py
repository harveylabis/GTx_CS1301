
#Write a function called inverted_sort. inverted_ should
#take as input a list of integers, and return as output a
#list with the integers sorted from HIGHEST to LOWEST.
#
#You may use any sorting algorithm you want: bubble, merge,
#insertion, selection, a new sort that you learned on your
#own, or even one you created yourself. You may use loops,
#or you may use recursion.
#
#You may not use Python's native list sort or reverse 
#methods; you must write your own sort.

import random

# using the selection sort
#Write your function here!
def inverted_sort(lst):
    for i in range(len(lst)):
        maxIndex = i
        for j in range(i+1, len(lst)):
            maxValue = lst[maxIndex]
            if  lst[j] > maxValue:
                maxValue = lst[j]
                maxIndex = j
        #Save the current minimum value since we're about
        #to delete it
        maxValue = lst[maxIndex]
        
        #Delete the minimum value from its current index
        del lst[maxIndex]
        
        #Insert the minimum value at its new index
        lst.insert(i, maxValue)
                
    return lst
                

#The code below will test your function. Feel free to
#modify it. As written originally, it will print the list:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
#print("testing for many values")
#print(inverted_sort([random.randint(1, 1000) for _ in range(10000)]))


