#An object's weight is defined as its mass times the gravity
#on the planet where it sits. We tend to assume that the
#planet is earth and its gravity is 9.807 m/s^2. However,
#sometimes we might want to calculate an object's weight on
#a different planet.
#
#Write a function called calculateWeight. calculateWeight
#should have three parameters: mass, planet, and gravity.
#planet and gravity should be keyword parameters: by
#default, they should take the values "Earth" (a string) and
#9.807 (a float). However, they should be able to be
#overriden to let us calculate weights on other planets.
#
#The function should return a string that looks like this:
#"A [mass] kg object weighs [weight] Newtons on [planet]."
#You should round the weight to two decimal points. You
#can do this by calling round() on the weight, e.g.
#roundedWeight = round(weight, 2). The 2 dictates how
#many decimal points should be included.
#
#For example:
#
# calculateWeight(10.0) ->
#       "A 10.0 kg object weighs 98.07 Newtons on Earth."
#
# calculateWeight(5.0, planet="Jupiter", gravity=24.79) ->
#       "A 5.0 kg object weighs 24.79 Newtons on Jupiter."
#
#Hint: If you're having trouble with creating the string to
#return, here's the first part:
#result = "A " + str(mass) + " kg object weighs " ...


#Write your function here!
def calculateWeight(mass, planet='Earth', gravity=9.807):
    result = "A {} kg object weighs {} Newtons on {}.".format(mass, round(mass*gravity, 2), planet)
    return result


#The lines of code below will test your function. They are
#not used for grading, so feel free to change them. As
#written, these lines should output the two lines of output
#shown above.
print(calculateWeight(10.0))
print(calculateWeight(5.0, planet="Jupiter", gravity=24.79))


