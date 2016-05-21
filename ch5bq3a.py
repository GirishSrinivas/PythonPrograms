import nltk
from nltk.corpus import brown as bn

def exercise3a(category):
	print "For category: " +category
	brown_tagged_words = bn.tagged_words(categories = category)
	brown_words = bn.words(categories = category)
	brown_tagged_plural = set([w for (w, t) in brown_tagged_words if t == 'NNS'])
	freq = nltk.FreqDist(brown_words)
	word_cnt_plural = [(w, freq[w]) for w in brown_tagged_plural]
	print "The Plural nouns are:"
	print word_cnt_plural
	wnl = nltk.WordNetLemmatizer()
	lemma_singular = [wnl.lemmatize(t) for t in brown_tagged_plural]
	print
	print
	print "The Singular nouns are:"
	word_cnt_singular = [(w, freq[w]) for w in lemma_singular]
	print word_cnt_singular
	print
	print

	#com_plural = set([w1 for (w1, t1) in word_cnt_plural for (W2,t2) in word_cnt_singular if t1 > t2])
	#print com_plural
	#print len(com_plural)


def main():
	print "Exercise3a"
	categories = ['humor', 'romance', 'government']
	for c in categories:
		exercise3a(c)


if __name__ == '__main__':
	main()