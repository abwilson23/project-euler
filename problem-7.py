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


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 7           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

