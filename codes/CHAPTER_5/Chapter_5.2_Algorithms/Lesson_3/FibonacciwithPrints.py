#As before, our core function below hasn't changed. What
#has changed is that we've added print statements so we can
#see a bit about how the program is running.

def fib(n):
    if n == 1 or n == 2:
        print("Found fib(", n, "): returning 1!", sep = "")
        return 1
    
    #As with the factorial function, we want to print every
    #time we're about to create a new call to Fibonacci,
    #and every time such a call is completed.
    
    else:
        print("Finding fib(", n, "): fib(", n - 1, ") + fib(", n-2, ")", sep = "")
        result =  fib(n - 1) + fib(n - 2)
        print("Found fib(", n, "): ", result, sep = "")
        return result

#Now if we run this, we'll see a lot more output. Feel free
#to change this line to visualize different Fibonacci
#numbers.
print("fib(5) is", fib(5))

#The output here is more complex; you may want to copy it
#into another window to read it.
#
#When fib(5) is first called, it wants to calculate fib(4)
#and fib(3). So, it calls fib(4) first, which demands fib(3)
#and fib(2). So, it calls fib(3), which demands fib(2) and
#fib(1). Those are both the base case, so both return 1.
#So, in the execution order, we see fib(5), then fib(4),
#then fib(3), then fib(2), then fib(1).
#
#Once fib(2) and fib(1) have run, then fib(3) can finish,
#and so the next statement printed is the result of fib(3).
#Once fib(3) is finished, then we can finish fib(4) by
#finding fib(2). fib(2) is again 1, so the next line is
#fib(2).
#
#Once fib(3) and fib(2) have finished, we can finish
#fib(4), so the next statement printed is the result of
#fib(4).
#
#Now that fib(4) is finished, we're all the way back to the
#first call, which wanted fib(4) + fib(3). Now, the rest of
#the execution is evaluating fib(3), which immediately
#demands fib(2) and fib(1). So, the next two lines are the
#results of fib(2) and fib(1). Once those are done, fib(3)
#is finished again.
#
#Now fib(4) and fib(3) are both finished, so the very first
#line can end: fib(4) + fib(3) = 3 + 2 = 5.


