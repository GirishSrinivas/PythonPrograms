# AUTHOR: GIRISH SRINIVAS

import nltk, re
from nltk.corpus import brown as bn

def question2(category):
	#print
	#print "For Category: " + category
	#print "Words with the tag 'JJ':"
	#print
	words = bn.tagged_words(categories = category)
	wordlist = bn.words(categories = category)
	words_JJ = set(sorted([(word, tag) for (word, tag) in words if tag == 'JJ']))
	print len(words_JJ)
	print
	print
	print "Words with tags 'VBZ' -> 3rd Person Singular Verbs or ('NNPS' or 'NNS') -> plural nouns:"
	print
	words_VBP_NNPS_NNS = [(word, tag) for (word, tag) in words if tag == 'VBZ' or tag == 'NNPS' or tag == 'NNS']
	print words_VBP_NNPS_NNS[:10]
	print
	print
	print "Ratio"
	print
	male_pattern = r'\bhe\b|\bhis\b|\bhim\b|\bhimself\b'
	female_pattern = r'\bshe\b|\bher\b|\bhers\b|\bherself\b'
	male_pronouns = len([w for w in wordlist if re.search(male_pattern, w.lower())])
	female_pronouns = len([w for w in wordlist if re.search(female_pattern, w.lower())])
	print "Male : Female is -> %d : %d" %(male_pronouns, female_pronouns)
	print
	print
	sent = ""
	print "3 word prepositional phrases are:"
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(words):
        if(t1.startswith('IN') and t2.startswith('AT') and t3.startswith('NN')):
            print w1, w2, w3
    print sent
	print
	print


def main():
	categories = ['humor', 'romance', 'government']
	for c in categories:
		question2(c)


if __name__ == "__main__":
    main()

