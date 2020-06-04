#Attempts to divide by zero
def divideByZero(): 
    print(1 / 0)

print("About to encounter an error...")
try:
    divideByZero()
except Exception as error:
    print(error)
print("We just encountered an error!")
