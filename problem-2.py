# Problem 2
# https://projecteuler.net/problem=2


def even_fibs(n):

    summe = 0
    a,b = 1,1

    while a < n:

        if a % 2 == 0:
            summe += a

        a,b = b, a + b
        
    return summe


# The evens_and_odds function is based off the fact that
# the sum of the evens = the sum of the odds if you end the 
# summation on an even fibonacci number.
#
# Consider the terms up to 8: 1, 1, 2, 3, 5, 8
# Now, 1 + 1 + 3 + 5 = 10 = 2 + 8

def evens_and_odds(n):

    summe = 0
    a,b = 1,1

    while a <= n:
        summe += a
        a,b = b, a + b

    return summe / 2


if __name__ == "__main__":

    print ("=================================")
    print ("*          Problem Two          *")
    print ("*         Andrew Wilson         *")
    print ("*********************************\n")

    print (even_fibs(4000000))
    print (evens_and_odds(4000000))
