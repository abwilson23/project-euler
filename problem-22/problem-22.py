# Problem 22
# https://projecteuler.net/problem=22

import sys

def find_names_score():
    names = []
    with open(sys.argv[1]) as f:
        names = [s[1:-1] for s in f.read().strip().split(',')]

    score = 0
    names.sort()
    for i, name in enumerate(names):
        score += name_score(name)*(i + 1)
    print (score)

def name_score(s):
    score = 0
    for x in s:
        score += ord(x) - 64
    return score
        
if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 22           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    find_names_score()
    
