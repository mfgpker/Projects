print "Factor Loaded"
def factorial(num):
	"""
    Prints factorial for a given number
    Recursive solution
    """
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)
print ""
print "factorial: "
print factorial(1)
print factorial(5)
print factorial(10)


def factorial2(num):
	"""
    Prints factorial for a given number
    Loop solution
    """
	factorial = 1
	if num == 0:
		return 1
	for i in range(1, num+1):
		factorial *= i
	return factorial
print ""
print "factorial2: "
print factorial2(1)
print factorial2(5)
print factorial2(10)