print "Counting vowels"

def Counting_vowels(sentence):
	count = 0
	vowels = "aeiuoyAEIOUY"
 	for letter in sentence:
		if letter in vowels:
			count += 1
	print (count)

def main():
	text = (raw_input("Please enter a string to count vowels: "))
	Counting_vowels(text)

main()