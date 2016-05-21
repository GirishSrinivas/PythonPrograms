import nltk
from nltk.corpus import brown as bn

def exercise3b(category):
	print
	print "For category: " +category
	brown_tagged_words = bn.tagged_words(categories = category)
	cfd = nltk.ConditionalFreqDist(brown_tagged_words)
	li = [w for (w,t) in brown_tagged_words]
	wrd_cnt = set([(w, len(cfd[w].keys())) for w in li])
	max = 0
	for(w,c) in wrd_cnt:
		if(c >= max):
			max = c

	print "Maximum number of tags: %d" %max
	word_tag = [w for (w,c) in wrd_cnt if c == max]
	for w in word_tag:
		print w
		print cfd[w].keys()
		print

	print
	print


def main():
	categories = ['humor', 'romance', 'government']
	for c in categories:
		exercise3b(c)

if __name__ == '__main__':
	main()