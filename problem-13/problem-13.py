# Problem 13
# https://projecteuler.net/problem=13

import sys

def digit_sum():

    nums = []

    with open(sys.argv[1]) as infile:
        for line in infile:
            nums.append(int(line))

    a = sum(nums)
    print (str(a)[0:10])


if __name__ == "__main__":

    print ("===================================")
    print ("||          Problem 13           ||")
    print ("||         Andrew Wilson         ||")
    print ("===================================\n")

    digit_sum()


