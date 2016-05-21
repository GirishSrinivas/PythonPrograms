from __future__ import division
import nltk, re, pprint

def determiner(str):
	pattern = r'\bthe\b|\bThe\b|\ba\b|\bA\b|\ban\b|\bAn\b'
	token = nltk.regexp_tokenize(str, pattern)
	print "Determiners are: ", token


def main():
	string = 'One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'
	determiner(string);


if __name__ == "__main__":
    main()