#Take a look at the three functions completely written
#below. It's your job to correctly call each function with
#the following parameters:
#
#  Function 1: the string "Black Horse and a Cherry Tree" 
#  Function 2: no parameters
#  Function 3: these five numbers: 80, 80, 95, 86, 79

#Function 1
def cherry_pie(song):
    if ("Cherry" in song):
        print("Sheee's my cherry pie")
    else:
        print("Huh... must be an American Pie.")

#Function 2
def should_I_go_to_Waffle_House():
    print(True)

#Function 3
def average_grades(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    average = sum / 5
    print(average)


#Add your function calls here! Don't change any of the
#code above.

cherry_pie("Black Horse and a Cherry Tree")
should_I_go_to_Waffle_House()
average_grades(80, 80, 95, 86, 79)

