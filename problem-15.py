# Problem 15
# https://projecteuler.net/problem=15

import math

def lattice_paths(n):

    # For a 20x20 grid we note that we must travel (D)own 20 times and to the (R)ight 20 times
    # So what we're counting is permutations of D's and R's (i.e. downs and rights)
    # There is a well established formula for counting permutations which gives, for an nxn grid

    paths = (math.factorial(2*n) / math.factorial(n)**2)
    return paths

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("||          Problem 15           ||")
    print ("||         Andrew Wilson         ||")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print (lattice_paths(20))

