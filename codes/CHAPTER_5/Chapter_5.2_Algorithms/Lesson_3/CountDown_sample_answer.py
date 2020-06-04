#The actual code in this problem is pretty straightforward:
#it's no more complex than anything you did in Chapter 3.3:

def count_down2(start):
    while start >= 0:
        print(start)
        start -= 1
        
#What's interesting here is the relationship between that
#function and the recursive one:
def count_down(start):
    if start <= 0:
        print(start)
    
    else:
        print(start)
        count_down(start - 1)
        
#Notice that both have a built-in stop condition: when
#start is no longer positive, the process ends. The while
#loop subtracts 1 from start and runs the loop again, while
#the recursive function subtracts 1 from start and calls the
#recursive function again. The process is very similar.
#
#So why would you do it recursively? Chances are, you
#wouldn't do this problem recursively, but there are problems
#that are far simpler to solve recursively than with a loop.



