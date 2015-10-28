# Problem 6
# https://projecteuler.net/problem=6


def sums():

    square_sum, sum_square = 0, 0

    for i in range(1, 101):

        square_sum += i
        sum_square += i**2

    return (square_sum**2 - sum_square)


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 6           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    print (sums())
