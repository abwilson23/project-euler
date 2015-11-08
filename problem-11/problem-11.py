# Problem 11
# https://projecteuler.net/problem=11

import sys


def search_grid():

    grid = [] 
    largest = 0
    
    with open(sys.argv[1]) as infile:
        grid = [[int(n) for n in line.split(' ')] for line in infile]
    
    for i in range(0, 20):
        for j in range(0, 20):
            if 20 - j > 3:
                temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
                largest = check(temp, largest)
            if 20 - i > 3:
                temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
                largest = check(temp, largest)
            if 20 - j > 3 and 20 - i > 3:
                temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
                largest = check(temp, largest)
            if 20 - i > 3 and j > 3:
                temp = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
                largest = check(temp, largest)
    
    print ("The maximal product is: {}".format(largest))
                

def check(t, l):
    if t > l:
        l = t
    return l


if __name__ == "__main__":

    print ("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print ("||          Problem 11           ||")
    print ("||        Andrew Wilson          ||")
    print ("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

    search_grid()
