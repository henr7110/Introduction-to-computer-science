##calculates the largest amount of nuggets at McDonalds that cannot be bought
##from combinations of 6,9 and 20 packs of nuggets

#not needed, but stores amounts that CAN be bought from combinations of 6,9 and 20 packs
save = []

#used to count packs of a:6 packs b:9 packs and c: 20 packs
a = 0
b = 0
c = 0

#amount of nuggets being checked for a solution 
n = 1

#variables used to check if 6 consecutive n-values can be made from combinations of a,b,c
#if you solve the diophantine equation n = 6a+9b+20c=n 6 times in a row, you can
#find all later values from itteraions of a. The maximum value that can't be made
#will therefore be found right before this sequence (when counter = 6 it is n-6)
state = 0
counter = 0

#asks the user for three package sizes (normally 6,9 and 20) and stores them in a tuple.
print 'write three package sizes for McNuggets seperated by enter'
packages = (int(raw_input()),int(raw_input()),int(raw_input()))

#goes through all combinations of a,b,c for a certain n and checks if the equation gives n:
for n in range(1, 150):   
        while (c < 20):
                while (b < 20):
                        while (a < 20):
                                a += 1
                                #checks if the equation is solved with these a,b,c
                                nuggets = (packages[0]*a)+(packages[1]*b)+(packages[2]*c)
                                remainder = n % nuggets
                                if (remainder == 0):
                                        #if it does the value is saved and the loop is exited to itterate n
                                        #also it is noted that a solution was found (state and counter)
                                        save.append (n)
                                        a = 7
                                        b = 7
                                        c = 7
                                        state = 1
                                        counter += 1
                        b += 1
                        a = 0
                c += 1
                b = 0
                a = 0
        #checks to see if this n gave a solution, if not, it resets counter
        if state == 0:
                counter = 0
        #if n could be made from a,b,c the state is reset but not the counter
        else:
                state = 0
        #when the counter reaches 6, all later n-values can be made and the
        #largest value which couldn't be made was n-6
        if counter == 6:
                print packages
                print 'given package sizes ' + str(packages[0]) + ', ' + str(packages[1]) + ', and ' + str(packages[2]) + ', the largest number of McNuggets that cannot be bought in exact quantity is: ' + str(n-6)
                break
        #before entering the loop again for a new n, all values are reset since
        #all values were set to 7 to exit the loop.
        c = 0
        b = 0
        a = 0
 

        

		
		
			
