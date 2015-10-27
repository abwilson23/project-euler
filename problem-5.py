# Problem 5
# https://projecteuler.net/problem=5

import time

def smallest_multiple():

    i = 20
    divisors = [20,19,18,17,16,15,14,13,12,11]

    while i <= 670442572800: # the product of all the divisors

        flag = True
        for d in divisors:
            if i % d != 0:
                flag = False
                break

        if flag:
            return i

        i += 20
        

def fast():

    # Breaking up the divisors into their prime factors we can
    # explicitly calculate the least common multiple of them.
    # For a description of the algorithm, go here: 
    # https://en.wikipedia.org/wiki/Least_common_multiple
        
    # Breaking up the divisors into primes and selecting the primes 
    # with the highest powers we get:

    return 19*17*13*11*7*5*(3**2)*(2**4)


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 5           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    start_time = time.time()
    print (smallest_multiple())
    print ("--- %s seconds ---\n" % (time.time() - start_time))

    new_start_time = time.time()
    print (fast())
    print ("--- %s microseconds ---" % (1000000*(time.time() - new_start_time)))
