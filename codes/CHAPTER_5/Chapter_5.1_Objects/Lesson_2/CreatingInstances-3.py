#Define the class Name
class Name:
    def __init__(self):
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"

#Define the class Person
class Person:
    def __init__(self):
        self.name = Name()
        self.eyecolor = "[no eye color]"
        self.age = -1

#Create a new Person and assign it to myPerson
myPerson = Person()
#Print myPerson's name's firstname
print(myPerson.name.firstname)
#Change myPerson's name's firstname to David
myPerson.name.firstname = "David"
#Print myPerson's name's firstname
print(myPerson.name.firstname)


