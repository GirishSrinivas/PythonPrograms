# AUTHOR: GIRISH SRINIVAS

from __future__ import division
import nltk, re, pprint


SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def exercise30():
	pstem = ""
	lstem = ""
	token = nltk.word_tokenize(SimpleText)
	porter = nltk.PorterStemmer()
	lancaster = nltk.LancasterStemmer()

	print
	print "Raw text:"
	print SimpleText
	for word in token:
		pstem = pstem + porter.stem(word) + " "
		lstem = lstem + lancaster.stem(word) + " "

	print
	print "Stemming of raw text using PorterStemmer"
	print pstem
	print
	print "Stemming of raw text using LancasterStemmer"
	print lstem



def main():
	exercise30()

if __name__ == "__main__":
    main()