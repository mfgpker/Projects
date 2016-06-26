def pow(a,b):
    if b == 0:
        return 1
        
    else:
        temp = pow(a,b/2)
        if b % 2 == 0:
            return temp * temp
        else:
            return temp * temp * a
            
print pow(2,2)

print pow(2,3)