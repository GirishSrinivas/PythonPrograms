# AUTHOR: GIRISH SRINIVAS

from __future__ import division
import nltk, re, pprint

def piglatin(word):
	split = word.split('a|e|i|o|u')
	print split

def main():
	word = 'Latin'
	piglatin(word);


if __name__ == "__main__":
    main()