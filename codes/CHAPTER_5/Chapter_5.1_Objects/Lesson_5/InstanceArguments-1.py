class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def capitalizeName(name):
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()

myPerson = Person(Name("David", "Joyner"), "brown", 30)
capitalizeName(myPerson.name)
print(myPerson.name.firstname)
print(myPerson.name.lastname)


