# Problem 1
# https://projecteuler.net/problem=1

def getMeTheMultiples():
    
    summe = 0

    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            summe += i

    return summe

            

    



if __name__ == "__main__":

    print ("=================================")
    print ("*          Problem One          *")
    print ("*         Andrew Wilson         *")
    print ("*********************************")

    print (getMeTheMultiples())
    
