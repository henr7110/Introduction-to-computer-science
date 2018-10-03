##program that finds the nth prime when asked by the user

#asks the use for a certain prime number
print 'which prime number do you want?'
n = int(raw_input())

#initialize variables
div = 2
check = 3
prime = []

#adds two and three to the list, and sets check to 5
#because only odd integers can be prime
#and that is the next odd integer after 3
prime.append (2)
prime.append (check)
check += 2

print 'please hold'

#itterates through all prime numbers up to the one asked by user
while len(prime) < n:

    #generates list of all integers up to the number being checked for prime
    for i in range (3,check):

        #stops if the number being checked for divisibility is greater than one half,
        #because later numbers won't divide evenly with check, so if i has reached this
        #it will be prime since no even number greater than 1 divides evenly with it. 
        if i > check/2:
            prime.append (check)
            check += 2
            break
        #checks if the diviser (i) divides evenly with the number being checked
        if check % i == 0:
        #if it does, it is not prime and it checks the next 
            check += 2
            break
#prints out the prime number asked for
print 'the ' + str(n) +'th prime number is'
print prime[n-1]

    
    
