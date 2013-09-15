print ("Lets count some words")

def count_words():
	text = str.lower(raw_input("Enter your text: "))
	count = 0
	for letter in text:
		if letter in " ":
			count += 1

	print(count)

count_words()