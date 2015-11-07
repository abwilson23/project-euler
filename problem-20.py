# Problem 20
# https://projecteuler.net/problem=20

import math

def factorial():

    fact_sum = 0

    for x in str(math.factorial(100)):
        fact_sum += int(x)

    print (fact_sum)


if __name__ == "__main__":

    print ("===================================")
    print ("||          Problem 20           ||")
    print ("||         Andrew Wilson         ||")
    print ("===================================\n")

    factorial()

