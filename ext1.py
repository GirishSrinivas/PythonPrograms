# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.book import *

def computeAverageWordLength(text):
	result = sum([len(w) for w in text])
	print "Sum of lenght of all words in text3 is: %d" %result
	print "Average word length of 'The book of Genesis' is: %f" %(result/float(len(text)))

def main():
	text = text3
	computeAverageWordLength(text)

if __name__ == '__main__':
	main()