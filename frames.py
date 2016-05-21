import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import framenet as fn

def frames(words):
	regex = r"(?i)"+words
	
	#print len(f)
	"""for w in f:
		name = w.name.split(".")[0];
		if words == name:
			print w.name, w.ID"""
	"""for w in names:
		if word == w:
			print w
			a = True
			print "word found" """
	f = fn.lus()
	word = words + ".n"
	nameSet = set()
	names = set([w.name for w in f])
	found_in_framenet = word in names
		
	if found_in_framenet:
            print "found"
            print found_in_framenet
        else:
            print "not found"	
		

	"""if(a):
		for syn in wn.synsets(words,pos='n'):
				nameSet=nameSet.union(set(syn.lemma_names))

		print nameSet
	else:
		print "Word not found"
		print "No synsets found" """

def main():
	words = raw_input("Enter a word: ")
	frames(words)

if __name__ == "__main__":
    main()