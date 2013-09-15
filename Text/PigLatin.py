print ("Lets play PigLatin..")

def piglatin():
	word = str.lower (raw_input("Insert your word: "))
	vowels = "aeiouy"

	pig = "ay"
	way = "way"

	first = word[0]

	if first in vowels:
		new = word + way
	else:
		new = word[1:] +first + pig

	print(new)

piglatin()