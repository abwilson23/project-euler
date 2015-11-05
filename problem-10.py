# Problem 10
# https://projecteuler.net/problem=10

import math

# Re-use function from p3
def prime_check(n):

    if n == 0 or n == 1:
        return False

    # Only need to check up until the square root of the number 
    end = int(math.sqrt(n)) 
    
    for i in range(2, end + 1):
        if n % i == 0:
            return False

    return True
    
def sum_some_primes():

    sump = 5
    
    for x in [x for x in range(5, 2000000, 2) if x % 2 != 0 or x % 3 != 0]:
        
        if prime_check(x):
            sump += x

    print (sump)


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 10           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    sum_some_primes()
