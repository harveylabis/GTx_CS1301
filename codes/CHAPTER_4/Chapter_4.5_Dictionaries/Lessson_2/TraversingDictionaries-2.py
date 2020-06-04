#Creates myDictionary with sprockets=5, widgets=11, cogs=3, gizmos=15, 
#gadgets=1
myDictionary = {"sprockets" : 5, "widgets" : 11, "cogs" : 3, "gizmos" : 15, 
                "gadgets" : 1}
for key in myDictionary.keys():
    value = myDictionary[key]
    if value < 5:
        print(key, "is less than 5:", value)


