#Define the class Person
class Person:
    #Create a new instance of Person
    def __init__(self):
        #Person's default values
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"
        self.eyecolor = "[no eye color]"
        self.age = -1

#Create a new Person and assign it to myPerson
myPerson = Person()
#Print myPerson's firstname
print(myPerson.firstname)
#Change myPerson's firstname to David
myPerson.firstname = "David"
#Print myPerson's firstname
print(myPerson.firstname)


