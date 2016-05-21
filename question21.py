# AUTHOR: GIRISH SRINIVAS

from __future__ import division
import nltk, re, pprint

from urllib import urlopen
from nltk import book
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn


def unknown(url):
	print
	text = urlopen(url).read()
	sub_string = set(re.findall(r'[a-z]+', text))
	english = set(w.lower() for w in nltk.corpus.words.words())
	all_unusual = sub_string.difference(english)
	print "Length of text: ", len(text)
	print "Length of unusual words for all words in text: " ,len(all_unusual)
	print

	tokens = nltk.word_tokenize(text)
	small_words = set(w.lower() for w in tokens if w.isalpha())
	unusual = small_words.difference(english)
	print "Set of tokens", len(tokens)
	print "Length of unusual words for tokens: " ,len(unusual)
	print
	
	l = nltk.WordNetLemmatizer()
	wordl = [l.lemmatize(t) for t in tokens]
	small_wordsl = set(w.lower() for w in wordl if w.isalpha())
	lunusual = small_wordsl.difference(english)
	print "lemmatized set of words: ", len(wordl)
	print "Length of unusual words for lemmatized words: " ,len(lunusual)
	print




def main():
	url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"
	unknown(url)



if __name__ == "__main__":
    main()