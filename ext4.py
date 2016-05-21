import nltk
from nltk.corpus import brown as bn

def token_frequency(token, category):
	words = bn.words(categories = category)
	fdist = nltk.FreqDist([w.lower() for w in words])
	freq = fdist.freq(token)
	print "Frequency of the token '%s' in category: '%s' is: %f" %(token ,category, freq)


def main():
	token = raw_input("Enter a token: ")
	category = ['lore', 'news']
	for c in category:
		token_frequency(token, c)


if __name__ == '__main__':
	main()