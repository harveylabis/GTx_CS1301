class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizeString(instring):
    instring = instring.upper()

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeString(myPerson.name.firstname)
capitalizeString(myPerson.name.lastname)
print(myPerson.name.firstname)
print(myPerson.name.lastname)


