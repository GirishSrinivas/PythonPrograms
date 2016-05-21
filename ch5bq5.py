# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.corpus import brown as bn

def findtags(tag_prefix, tagged_text):
     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
     return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())


def exercise5(category):
	print 
	print "For category: " +category
	tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories = category))
	for tag in sorted(tagdict):
		print tag
	print

def main():
	print "Exercise 5"
	categories = ['humor', 'romance', 'government']
	for c in categories:
		exercise5(c)

if __name__ == '__main__':
	main()