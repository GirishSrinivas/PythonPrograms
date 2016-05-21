import nltk
from nltk.corpus import brown as bn

def lookupTagger(i):
	brown_tagged_sents = bn.tagged_sents(categories='news')
	brown_sents = bn.sents(categories='news')
	fd = nltk.FreqDist(bn.words(categories = 'news'))
	cfd = nltk.ConditionalFreqDist(bn.tagged_words(categories = 'news'))
	most_freq_words = fd.keys()[:i]
	likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
	baseline_tagger = nltk.UnigramTagger(model=likely_tags)
	evalResult = baseline_tagger.evaluate(brown_tagged_sents)
	print "Evaluation of lookupTagger for the size %d is: %f" %(i, evalResult)



def main():
	size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
	for s in size:
		lookupTagger(s)

if __name__ == '__main__':
	main()