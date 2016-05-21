import nltk
from nltk.book import *

def freqOfLetters(text):
	word4 = [w for w in text if len(w) == 4]
	fdist = FreqDist(word4)
	print fdist.keys()[:5]

def main():
	text = text5
	freqOfLetters(text)

if __name__ == '__main__':
	main()