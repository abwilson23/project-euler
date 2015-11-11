# Problem 12
# https://projecteuler.net/problem=12

import time

def find_tri_num():

    with open("primes1.txt") as infile:
        primes = [int(x) for x in infile.read().split()]

    i, factors = 1, 0
    while factors < 500:
        num = i*(i+1)/2
        factors = num_of_factors(primes, num)
        i += 1

    print (num)


def num_of_factors(primes, num):

    pfactors = []
    for x in primes:
        while num % x == 0:
            pfactors.append(x)
            num /= x
        if num == 1:
            break

    fact_pows = {}
    for p in pfactors:
        if p in fact_pows:
            fact_pows[p] += 1
        else:
            fact_pows[p] = 1

    factors = 1
    for k in fact_pows:
        factors *= (fact_pows[k] + 1)

    return factors


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("||          Problem 12           ||")
    print ("||         Andrew Wilson         ||")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    start_time = time.time()
    find_tri_num()
    print ("--- %s seconds ---" % (time.time() - start_time))


