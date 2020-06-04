#Right now, the code below will encounter an error when num
#is 0, but it will not print anything when it does, and then
#it will keep running for num = 1, num = 2, and num = 3
#afterwards. Modify this code so that once it hits an error,
#the loop stops altogether.
#
#You still should not print anything when the error is
#encountered, and the loop definition on line 10 should not
#be changed.

try:
    for num in range(-3, 3):
	    print(5 / num)
except:
    pass



