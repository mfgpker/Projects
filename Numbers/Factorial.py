def Factorial(n):
     if n == 0:
        return 1
     return n * Factorial(n-1)
     
def Factorial1(n):
     if n == 0:
        return 1
     sum = 1
     for i in range(1,n+1):
         sum = i * sum
     return sum
     
     
     
     
for i in range(0,10):
    print "rec Factorial = " + str(Factorial(i)) + " = ("+str(i)+") = " + str(Factorial1(i)) + " Factorial"