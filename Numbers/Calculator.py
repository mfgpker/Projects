print "Calculator Loaded"
def calc():
	x = int (raw_input("Please input the first integer: "))
	y = int (raw_input("Please input the second integer: "))
	type = str.lower(raw_input("(A)dd, (S)ubtract, (M)ultiply, (D)ivide : "))
	if type != "a" and type != "s" and type != "m" and type != "d":
		print ("Sorry, the command you entered is not valid.")
		calc();
	else:
		if type == "a":
			print ("The result is '" + str(x + y) + "'")
		elif type == "s":
			print ("The result is '" + str(x - y) + "'")
		elif type == "m":
			print ("The result is '" + str(x * y) + "'") 
		elif type == "d":
			if y != 0:
				print ("The result is '" + str(float(x) / float(y)) + "'")
			else:
				print ("Error! you can't divede with 0!")

		if str.lower (raw_input("Would you like to perform another calculation? ")) == "y":
			calc();
		else:
			exit([0])
calc()