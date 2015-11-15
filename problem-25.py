# Problem 25
# https://projecteuler.net/problem=25

def find_fib():

    fibs = [1, 1]
    while len(str(fibs[-1])) != 1000:
        fibs.append(fibs[-2] + fibs[-1])
    print(len(fibs))

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 25           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    find_fib()
    
