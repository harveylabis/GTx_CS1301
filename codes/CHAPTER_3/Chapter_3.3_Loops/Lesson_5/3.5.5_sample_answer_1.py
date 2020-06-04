beats_per_measure = 4
measures = 5

#-----------------------------------------------------------
#There are two tricky parts of this problem. We should
#generally know that we want two for loops, one inside the
#other. One will count from 1 to beats_per_measure, one will
#count from 1 to measures.
#
#Which one goes first though? Well, the inside loop runs
#several times for each run of the outer loop. So, do we want
#to go through 5 measures for each beat, or 4 beats for each
#measure?
#
#We want the latter. So, we want the beats loop _inside_ the
#measures loop.
#
#So, we start with the measures loop:

for measure in range(0, measures):
    
    #Above we see the second tricky part of this question.
    #If we looped from 1 to measures, we would loop one too
    #few times. So, we can start at 0, or we can start at 1
    #and go to measures + 1. Here it doesn't really matter
    #which we choose.
    
    for beat in range(1, beats_per_measure + 1):
        
        #Here, however, it does. If we want to print beat,
        #then we want it to start at 1. If we start at 1 and
        #run to beats_per_measure, though, it will run one too
        #few times. So, we go from 1 to beats_per_measure + 1.
        #
        #Then, we just print the current beat:
        
        print(beat)
        
        #We could also loop from 0 to beats_per_measure and
        #print beat + 1 instead.





