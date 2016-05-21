import nltk
from nltk.corpus import brown as bn

def func2(category):
	print
	sent = ""
	print "3 word prepositional phrases are:"
	words = bn.tagged_words(categories = category)
	for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(words):
		if(t1.startswith('IN') and t2.startswith('AT') and t3.startswith('NN')):
			#print w1, w2, w3
			sent = sent + w1.lower() + " " + w2.lower() + " " + w3.lower() + "."
	#print sent
	sent_part = sent.split(".")
	fd = nltk.FreqDist(sent_part)
	v = fd.most_common(3)
	print v
	#print sent_part
	print
	print


def main():
	categories = ['humor', 'romance', 'government']
	for c in categories:
		func2(c)


if __name__ == "__main__":
    main()
