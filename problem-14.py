# Problem 14
# https://projecteuler.net/problem=14

import time

def collatz(n):

    if n in book:
        return book[n]
    else:
        t = collatz(step(n)) + 1 
        book[n] = t
        return t

def step(n):

    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

def longest_cseq():

    for i in range(1, 1000000, 2):
        if i not in book:
            book[i] = collatz(i)

    print (max(book, key=book.get))

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 14           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    book = {1:1}
    start = time.time()
    longest_cseq()
    print ("--- {} seconds ---".format(start - time.time()))
