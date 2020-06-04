#Write a function called is_prime. is_prime should take
#as input one integer. It should return True if the integer
#is prime, False if the integer is not prime. You may
#assume the integer will be greater than 2 and less than
#1000.
#
#Remember, a prime number is one into which no number is
#divisible besides 1 and itself. For example, 6 is not
#prime because it is divisible by 2 and 3. 7 is prime
#because it is only divisible by 1 and itself.
#
#HINT: Remember, once you find a _single_ factor of the
#number, you can return False: it only takes one factor
#to make the number not prime.


#Add your code here!
def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
            
    return True


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, True, False
print(is_prime(5))
print(is_prime(6))
print(is_prime(97))
print(is_prime(105))
print(is_prime(997))
print(is_prime(999))






