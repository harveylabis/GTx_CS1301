seatingChart = {"David" : 3, "Lucy" : 3, "Dana" : 2,
                "Addison" : 2, "Vrushali" : 1, "Bilbo" : 3,
                "Sara" : 1, "Lugos" : 1, "Mireia" : 1,
                "Partha" : 2, "Venijamin" : 1, "Terra" : 2, 
                "Tryphon" : 3, "Gevorg" : 1, "Raza" : 3,
                "Rein" : 3, "Sofia" : 2, "Perle" : 2}

#For each name, table pair in the seating chart
for (name, table) in seatingChart.items():  
    #Print the table for the name
    print(name, " is seated at table #", table, sep="")  

print()
#For each table number
for i in range(1, 4):   
    print("The guests at table #", i, " are: ", sep="", end="")
    #For each name, table pair
    for (name, table) in seatingChart.items():  
        #If the table numer is this number
        if i == table:  
            #Print the name
            print(name, end=" ")    
    print()


