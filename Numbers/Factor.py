print "Factor Loaded"

def factor(x):
	i = 0
	f = 1
	while i <= x:
		i+=1
		f*=i
	return f

def main():
	x = int (raw_input("Please input the first integer: "))
	print (str(factor(x)))

main()