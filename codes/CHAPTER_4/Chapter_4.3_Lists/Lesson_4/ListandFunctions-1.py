#Averages each list in in2DList
def TwoDAverageWithPop(in2DList):  
    result = []
    #Repeat until in2DList is empty
    while len(in2DList) > 0:    
        #Remove and assign the last item of in2DList to numList
        numList = in2DList.pop()    
        sum = 0
        count = 0
        #Repeat until numList is empty
        while len(numList) > 0: 
            #Remove and save the last item of numList to number
            number = numList.pop()  
            sum += number
            count += 1
        #Insert this average at the beginning of result
        result.insert(0, sum / count)   
    return result

my2DList = [[91, 95, 89, 92, 85],[85, 87, 91, 81, 82],
            [79, 75, 85, 83, 89],[81, 89, 91, 91, 90],
            [99, 91, 95, 89, 90]]

print("Averages:", TwoDAverageWithPop(my2DList))
print("my2DList:", my2DList)


