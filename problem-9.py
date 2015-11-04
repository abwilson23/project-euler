# Problem 9
# https://projecteuler.net/problem=9

import math

def pythagorean_trip():

    a = [(a,b, math.sqrt(a**2 + b**2)) for a in range(1, 1000) for b in range(1, 1000)
            if (a + b + math.sqrt(a**2 + b**2)) == 1000 and natural([a,b, math.sqrt(a**2 + b**2)])]

    t = a[0]
    print (a)
    print (t[0]*t[1]*t[2]) 


def natural(l):
    for x in l:
        if x not in range(0,1000):
            return False
    return True    


if __name__ == "__main__":

    print ("===================================")
    print ("||           Problem 9           ||")
    print ("||         Andrew Wilson         ||")
    print ("===================================\n")

    pythagorean_trip()

