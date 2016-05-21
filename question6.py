# AUTHOR: GIRISH SRINIVAS

from __future__ import division
import nltk, re, pprint

def pattern(string):
	patternb = r'[A-Z][a-z]*'
	patternc = r'p[aeiou]{,2}t'
	patternf = r'\w+|[^\w\s]+'
	partb = nltk.regexp_tokenize(string, patternb)
	partc = nltk.regexp_tokenize(string, patternc)
	partf = nltk.regexp_tokenize(string, patternf)
	print "Pattern for regexp 1" ,partb
	print
	print "Pattern for regexp 2" ,partc
	print
	print "Pattern for regexp 3" ,partf



def main():
	string = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
	pattern(string);


if __name__ == "__main__":
    main()