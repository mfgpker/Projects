def GCD(a,b):
    if (a < b):
        return GCD(b,a)
    elif (b==0):
        return a
    else:
        return GCD(b, a % b)
    
    
print (GCD(8, 5))