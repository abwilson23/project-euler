# Problem 3
# https://projecteuler.net/problem=3

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
    

def prime_factor(n):

    if prime_check(n): # First, check if the number is prime
        return n

    a = 2
    factors = []

    while a <= n: # Create a list of factors, shrinking n as you go

        if n % a == 0:
            factors.append(a)
            n /= a
        a += 1
    
    final = [i for i in factors if prime_check(i)]
    return final[-1]


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem Two          |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print (prime_factor(600851475143))
