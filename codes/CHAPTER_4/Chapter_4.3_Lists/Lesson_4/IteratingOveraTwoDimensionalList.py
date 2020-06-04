#Averages the numbers in a list
#Averages each list in in2DList
def TwoDAverage(in2DList):  
    result = []
    #For each list in the list of lists
    for numList in in2DList:    
        sum = 0
        #For each number in the current list
        for number in numList:  
            sum += number
        #Append this list's average to result
        result.append(sum / len(numList))   
    return result

my2DList = [[91, 95, 89, 92, 85],
          [85, 87, 91, 81, 82],
          [79, 75, 85, 83, 89],
          [81, 89, 91, 91, 90],
          [99, 91, 95, 89, 90]]

print("Averages:", TwoDAverage(my2DList))


