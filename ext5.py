def stringFunction(string):
	print
	print "Input string is: %s" %string
	print
	bland = string.split()
	print "The split string is: "
	print bland
	print
	secondLetter = ''
	for i in range(len(string)):
		if i == 0:
			secondLetter = secondLetter + string[i + 1]
		if string[i] == ' ':
			secondLetter = secondLetter + string[i + 2]
	print "Every second letter is: %s" %secondLetter
	print
	space = ' '
	newString = space.join(bland)
	print "The joined letters are: %s" %newString
	print
	order = string.split()
	order.sort()
	print "Alphabetical order of the input string is: "
	for i in order:
		print i
	print


def main():
	silly = 'newly formed bland ideas are inexpressible in an infuriating way'
	input2 = 'colorless green ideas sleep furiously'

	stringFunction(silly)
	stringFunction(input2)

if __name__ == '__main__':
	main()