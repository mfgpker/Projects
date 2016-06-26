def Factorial(n):
     if n == 0:
        return 1
     return n * Factorial(n-1)

def printE(n):
    e = 0.0
    for k in range(0, n):
        e = e + 1.0/(Factorial(k))
        #print "e("+str(k)+") = " + str(e) 
    p = "{0:."+str(n)+"f}"
    print( p.format(e))


printE(1)
printE(2)
printE(3)
printE(4)
printE(5)
printE(6)
printE(7)
printE(8)
printE(9)
printE(10)

