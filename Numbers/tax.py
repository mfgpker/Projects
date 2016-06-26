def tax(price, tax):
    t = (price / 100.0) * tax 
    totalprice = price + t
    return totalprice, t
    


print tax(199, 25)