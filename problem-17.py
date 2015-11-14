# Problem 17
# https://projecteuler.net/problem=17

from num2words import num2words

def count_letters():
    letter_count = 0
    for i in range(1, 1001):
        letter_count += len(filter(lambda s: s not in ' -', num2words(i)))

    print (letter_count)

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 17           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    count_letters()
