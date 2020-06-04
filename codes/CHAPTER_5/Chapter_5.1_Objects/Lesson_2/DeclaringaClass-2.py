#Define the class Name
class Name:
    def __init__(self):
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"

#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self):
        #Person's default values
        self.name = Name()
        self.eyecolor = "[no eye color]"
        self.age = -1

harvey = Person()
print(harvey.name.firstname)
        
        