# Implementing a Student class for debugging
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

student1 = Student("Harvey", "Abiagador")
student2 = Student("John Cristian", "Badilla")
student3 = Student("Ronnie", "Naquila")
student4 = Student("Vince Daniel", "Villalba")
student5 = Student("Jommel", "Yandug")



stud_lst = [student1, student2, student3, student4, student5]





#Imagine you're writing a program to check attendance on a
#classroom roster. The list of students in attendance comes
#in the form of a list of instances of the Student class.
#
#You don't have access to the code for the Student class.
#However, you know that it has at least two attributes:
#first_name and last_name.
#
#Write a function called check_attendance. check_attendance
#should take three parameters: a list of instances of
#Student representing the students in attendance, a first
#name as a string, and a last name as a string (in that
#order).
#
#The function should return True if any instance in the
#list has the same first and last name as the two
#arguments. It should return False otherwise.
#
#You may assume that the list of students is sorted
#alphabetically, by last name and then by first name. This
#allows you to solve this with a binary search. However,
#you may also solve this problem with a linear search if
#you would prefer.

# Linear Search
#Write your function here!
""" def check_attendance(roster_lst, f_name, l_name):
    for student in roster_lst:
        if student.first_name == f_name and student.last_name == l_name:
            return True
    return False """

# Binary Search
# Write your function here!
def check_attendance(roster_lst, f_name, l_name):
    if len(roster_lst) == 0:
        return False
    search_for = l_name + ' ' + f_name
    names = [student.last_name + ' ' + student.first_name for student in roster_lst]
    print(names)
    midIndex = len(roster_lst)//2
    if names[midIndex] == search_for:
        return True
    if names[midIndex] < search_for: # if True, it belongs to higher half, recursively call with higher half
        return check_attendance(roster_lst[midIndex+1:], f_name, l_name)
    else: # if above is False, it belongs to lower half, recursively call with lower half
        return check_attendance(roster_lst[:midIndex], f_name, l_name)


#If you would like, you may implement the Student class as
#described and use it to test your code. This is not
#necessary to complete the problem, but it may help you
#debug. If you create a Student class, all you need is
#a constructor that assigns values to two attributes:
#self.first_name and self.last_name.

print(check_attendance(stud_lst, "Jommel", "Yandug"))
print(check_attendance(stud_lst, "Meriam", "Abiagador"))


