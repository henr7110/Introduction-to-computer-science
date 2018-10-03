##program that finds the sum of a log of primes up to a number n
##and finds the ration between the sum and the nth prime. 

from math import *

#initialize variables
div = 2
check = 3
prime = []

#asks the use for a certain prime number
print 'what shall n be?'
n = int(raw_input())

#the loop only works after prime number 5,
#so these are added to the prime array
prime.append (2)
prime.append (check)
check += 2

print 'please hold'

#counts through all prime numbers up to the one asked by user
while len(prime) < n:

    #generates list of all integers up to the number being checked for prime
    for i in range (3,check):

        #the number is prime if no integers divide evenly with it
        #up till 1/2 the number
        if i > check/2:
            prime.append (check)
            check += 2
            break
        
        #checks if the diviser (i) divides evenly with the number being checked
        #if it does, it is not prime and it moves to check the next 
        if check % i == 0:
            check += 2
            break

#takes log to all prime numbers in prime array
logprime = [log(x) for x in prime]

#calculates and prints the ratio
ratio = sum(logprime [:-1])/prime[-1]
            
print 'ratio is ' + str(ratio)

