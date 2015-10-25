# Problem 4
# https://projecteuler.net/problem=4


def check_palindrome(n):

    p = list(str(n))

    for i in range(0, len(p) / 2):

        if p[i] != p[len(p) - 1 - i]:
            return False

    return True


def find_palindrome():

    i = 999
    palindromes = []

    # Can restrict our search b/c we know there exists a palindrome in this range
    while i > 750: 
        j = 999
        while j > 750:
            if check_palindrome(i*j):
                palindromes.append(i*j)
            j -= 1
        i -= 1

    print (max(palindromes))


if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|           Problem 4           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    find_palindrome()

