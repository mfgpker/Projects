print "Palindrome loaded"

def Palindrome ():
	text = str.lower (raw_input("Please input a string: "))
	while text == "" :
		text = str.lower (raw_input("Please input a string: "))
	text2 = text[::-1]
	if text == text2:
		print (text + " : "+ text2 + " is a palindrome word.")
	else:
		print (text + " : "+ text2 + " is not a palindrome word.")

Palindrome ()