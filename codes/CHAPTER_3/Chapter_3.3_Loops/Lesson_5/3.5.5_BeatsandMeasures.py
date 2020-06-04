beats_per_measure = 4
measures = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In music, a song's time signature is given in terms of beats
#per measure. A common time signature is 4 beats per measure:
#for every measure of music, a conductor might count from 1
#to 4 with the tempo of the music.
#
#A song then has a number of measures. For example, a short
#song might have only 5 measures. In which case, a conductor
#would count from 1 to 4 five times. If the time signature had
#instead been 3 beats per measure, she would could from 1 to 3
#five times instead.
#
#Write a nested for loop that will print out the beats of the
#piece of music. For example, if the song had 4 beats per
#measure and only 2 measures, this would print out:
#
#1
#2
#3
#4
#1
#2
#3
#4
#
#We print from 1 to 4 before starting over because there are
#4 beats per measure, and we print them all twice because there
#are two measures.


#Add your code here! Using the original values of the variables
#above, this will initially print 1 through 4 five times for a
#total of 20 lines.
for measure in range(measures):
    for beats in range(1, beats_per_measure+1):
        print(beats)





