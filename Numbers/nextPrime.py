import math


def boollistmaker(n):
    listofzeros = [True] * n
    return listofzeros
    
def Primes(n):
    A = boollistmaker(n)
    A[0] = A[1] = False
    print int(math.sqrt(n))
    for i in range(2, int(math.sqrt(n))):
        if (A[i] == True):
            for j in range((i**2), n-1):
                A[j] = False
    return A
    
    
def is_prime(n):
    if (n <= 1):
        return False
    elif (n <= 3):
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    else:
        i = 5
        while i*i <= n:
            if (n % i == 0 or n % (i+2) == 0):
                return False
            i += 6
        return True
    

con = True
i = 1
while con:
    isPrime = is_prime(i)
    if isPrime:
        print "Prime: " + str(i)
        
        
        input = raw_input("continue? (y/n)")
        if input == "y":
            con = True
        else:
            con = False
    i += 1  