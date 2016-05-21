# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.corpus import brown as bn

def parta():
	print
	print
	total_brown_tagged_words = bn.tagged_words()
	cfd1 = nltk.ConditionalFreqDist(total_brown_tagged_words)
	set1 = set([a for (a, b) in total_brown_tagged_words])
	for s in set1:
		if(len(cfd1[s].keys()) == 5):
			print s

	print
	print


def partb():
	print
	print
	tags = [b for (a, b) in bn.tagged_words()]
	fd = nltk.FreqDist(tags)
	ft = fd.keys()
	cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in bn.tagged_words())

	for a in ft:
		if fd[a] == 1:
			print "For POS: " +a
			print cfd2[a].keys()
			print

	print
	print


def main():
	parta()
	partb()

if __name__ == "__main__":
    main()