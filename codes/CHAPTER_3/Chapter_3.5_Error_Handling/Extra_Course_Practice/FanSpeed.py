#Imagine you're writing the software that controls the speed
#of a ceiling fan. The user changes the fan's speed by
#pulling a string. Pulling the string increases the fan's =
#speed by 1, unless it's already at the maximum speed. If
#it's already at the maximum speed, it changes the speed
#back to 0.
#
#Write a function called pullString. pullString should take
#two parameters: a current speed, and a maximum speed, both
#integers. pullString should return the new fan speed
#according to the reasoning above.

#You may assume that the input will be integers. You should
#also assume that the fan's speed *can* equal the maximum
#speed, but it *cannot* exceed the maximum speed. You may
#thus assume that you will never be given a currentSpeed
#higher than maxSpeed.


#Write your function here!
def pullString(current_speed, maximum_speed):
    if current_speed == maximum_speed:
        return 0
    else:
        current_speed += 1
        return current_speed

#The code below will test your function. It isn't used for
#grading, so you can change or remove it if you'd like. As
#written, these three lines should print 3, 5, and 0.
print(pullString(2, 5))
print(pullString(4, 5))
print(pullString(7, 7))


