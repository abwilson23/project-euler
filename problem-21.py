# Problem 21
# https://projecteuler.net/problem=21

def amicable_nums():
    a_sum = 0
    for i in range(1, 10000):
        if d(d(i)) == i and i != d(i):
            a_sum += i
    print (a_sum)

def d(n):
    fsum = 0
    for div in range(1, n/2 + 1):
        if n % div == 0:
            fsum += div
    return fsum

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 21           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    amicable_nums()
    
