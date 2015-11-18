# Problem 30
# https://projecteuler.net/problem=30

def digit_powers():

    digit_sum = 0
    for i in range(2, 5*(9**5)): 
        if sum([int(x)**5 for x in str(i)]) == i:
            digit_sum += i
    print (digit_sum)

if __name__ == "__main__":

    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("|          Problem 30           |")
    print ("|         Andrew Wilson         |")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    digit_powers()

