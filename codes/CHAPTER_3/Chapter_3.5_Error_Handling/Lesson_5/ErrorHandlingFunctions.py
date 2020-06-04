#Attempts to divide by zero
def divideByZero(): 
    try:
        print(1 / 0)
    except Exception as error:
        print(error)

print("About to encounter an error...")
divideByZero()
print("We just encountered an error!")
