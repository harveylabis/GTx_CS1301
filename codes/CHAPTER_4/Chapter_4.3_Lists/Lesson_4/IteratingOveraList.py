#Averages the numbers in a list
def average(inList):
    sum = 0
    for number in inList:
        sum += number
    return sum / len(inList)

myList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myList2 = [97, 87, 91, 83, 85, 91, 95, 99, 81, 85]

print("The average of myList1 is:", average(myList1))
print("The average of myList2 is:", average(myList2))


