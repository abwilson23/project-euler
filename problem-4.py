# Problem 4
# https://projecteuler.net/problem=4


def find_palindrome():

    pal = 0

    # Can restrict our search b/c we want 3-digits factors 
    for i in range(999, 100, -1): 
        for j in range(999, 100, -1):
            if str(i*j) == str(i*j)[::-1]:
                if i*j > pal:
                   pal = i*j 

    print (pal)


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 4           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    find_palindrome()

