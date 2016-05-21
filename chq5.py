import nltk
from nltk.corpus import brown as bn

def func(category):
	words = bn.tagged_words(categories = category)
	for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(words):
		if(t1.startswith('IN') and t2.startswith('AT') and t3.startswith('NN')):
			print w1, w2, w3


def main():
	categories = ['humor', 'romance', 'government']
	for c in categories:
		func(c)

if __name__ == "__main__":
    main()
