import math

def pi(n):
	return (n * math.sin(math.radians(180)/n))

def printPI(n):
    p16 = 1
    pi = 0
    for k in range(0, n):
        pi = pi + 1.0/p16 * (4.0/(8*k + 1) - 2.0/(8*k + 4) - 1.0/(8*k + 5) - 1.0/(8*k+6))
        p16 = p16 * 16
    p = "{0:."+str(n)+"f}"
    print(p.format(pi))

printPI(1)

printPI(2)

printPI(3)

printPI(111)