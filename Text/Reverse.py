print "Reverse a string"

def Reverse():
	text = (raw_input("Please input a string: "))
	text2 = text[::-1]
	print(text + " : " + text2)
	

Reverse()