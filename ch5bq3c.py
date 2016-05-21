# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.corpus import brown as bn

def exercise3c(category):
	print
	print "For category: " +category
	brown_tag_words = bn.tagged_words(categories = category)
	tag_fd = nltk.FreqDist(t for (w,t) in brown_tag_words)
	print tag_fd.keys()[:10]
	print


def main():
	categories = ['humor', 'romance', 'government']
	for c in categories:
		exercise3c(c)

if __name__ == '__main__':
	main()