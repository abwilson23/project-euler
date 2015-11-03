# Problem 16
# https://projecteuler.net/problem=16


def digit_sum():
    
    d_sum = 0
    digits = [int(x) for x in str(2**1000)]

    for x in digits:
        d_sum += x

    print (d_sum)


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 16           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    digit_sum()
