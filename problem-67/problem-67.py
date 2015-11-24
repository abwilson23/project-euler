# Problem 67
# https://projecteuler.net/problem=67

import sys, time

def max_path():

    tree = []
    with open(sys.argv[1]) as infile:
        tree = [[int(x) for x in line.split(' ')] for line in infile]

    print(bottom_up_iter(tree, len(tree)))


def bottom_up_iter(tree, l):

    h = l - 2
    while h >= 0:
        for i in range(0, len(tree[h])):
            tree[h][i] += max(tree[h + 1][i], tree[h + 1][i + 1])
        h -= 1

    return tree[0][0]


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 67           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    start = time.time()
    max_path()
    print("---- {} s ----".format(time.time() - start))
