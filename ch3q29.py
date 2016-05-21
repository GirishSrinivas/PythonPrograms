from __future__ import division
import nltk, re, pprint
from nltk.corpus import brown


def Automated_Readability_Index(section):
	sents = len(brown.sents(categories = section))
	words = len(brown.words(categories = section))
	text = " ".join(brown.words(categories = section))
	letters = len(text)
	uw = letters / float(words) 
	us = words / float(sents) 
	ari = (4.71 * uw) + (0.5 * us) - 21.43
	return ari



def main():
	for section in brown.categories():
		print section + " : %f" %Automated_Readability_Index(section)

if __name__ == "__main__":
    main()