#A common formula in probability and statistics is the
#formula for the number of possible combinations of r
#objects from a set of n objects. For example, the question,
#"How many possible 2-card hands can you deal from a deck of
#52 unique cards?" is saying, "How many combinations of 2
#can you make from a set of 52?"
#
#The formula for the number of combinations of length r from
#a set of n objects is:
#
#  numCombinations = n! / r!(n-r)!
#
#The ! mark is the symbol for factorial. Factorial means the
#product of the number times every number between itself and
#1. For example, 5! is 120: 5 * 4 * 3 * 2 * 1 = 120.
#
#Write a function called numCombinations with two parameters:
#n, the number of objects from which to choose, and r, the
#number of objects to choose. numCombinations should return
#the number of combinations according to the formula above.
#Don't worry if you don't fully understand what combinations
#are -- just focus on implementing a function that solves
#that formula given n and r.
#
#You may *not* use Python's built-in factorial method to
#complete this; you should implement that yourself.
#
#Hint: We'd suggest writing two functions: factorial() and
#numCombinations(). Then, call factorial() in your code for 
#numCombinations(). You don't have to do this, but it will
#make your answer a little easier!
#
#Hint 2: Remember to put parentheses around the denominator.


#Write your numCombinations function (and any other functions) 
#here!

def factorial(num):
    if num == 0:
        return 1
    return (num * factorial(num - 1))

def numCombinations(n, r):
    # formula: n! / r!(n-r)!
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    
    total_combinations = n_factorial / (r_factorial * n_r_factorial)
    
    return int(total_combinations)

#The lines below will test your code. They are not used for
#grading, so feel free to modify them. As written, they should
#print: 1326.0, 252.0, and 4.0, each on their own line.
print(numCombinations(52, 2))
print(numCombinations(10, 5))
print(numCombinations(4, 1))


