myList1 = ["One", "Two", "Three"]
myList2 = ["One", "Two", "Three"]
 
print(id(myList1) == id(myList2))
 
myList2.append("Four")
 
print(myList1)
print(myList2)
