# Problem 7
# https://projecteuler.net/problem=7

import math

def prime_check(n):

    if n == 0 or n == 1:
        return False

    # Only need to check up until the square root of the number 
    end = int(math.sqrt(n)) 
    
    for i in range(2, end + 1):
        if n % i == 0:
            return False

    return True

def find_prime():

    i = 2
    primes = []

    while len(primes) < 10001:
        
        if prime_check(i):
            primes.append(i)
        i += 1

    return primes[-1]

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 7           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print find_prime()
