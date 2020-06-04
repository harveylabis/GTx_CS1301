grades  = [100, 95, 93, 91, 90, 89,
            87, 87, 85, 85, 84, 82]

total_sum = 0
count = 0
for grade in grades:
    count = count + 1
    total_sum = total_sum + grade
    print("Current sum: ", total_sum)
 
print(total_sum/count)