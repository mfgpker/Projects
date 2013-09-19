
def findthecost(w, h, prise):
	Areal = w*h
	Cost = Areal * prise
	return ("The total cost is " + str(Areal) + " kr. for " + str(Cost) + "square meter")

def main():
	w = int(raw_input("What's the width of the floor? "))
	h = int(raw_input("What's the height of the floor? "))
	p = int(raw_input("What's the cost per sq. meter? "))
	print findthecost(w, h, p)

if __name__ == '__main__':
	main()