# AUTHOR: GIRISH SRINIVAS

import nltk, random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000] 


def document_features4a(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
    	if len(wn.synsets(word)) > 0:
    		features['contains(%s)' % word] = 'KNOWN'
    	else:
    		features['contains(%s)' % word] = 'UNK'
    return features


def main():
	documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
	random.shuffle(documents)
	featuresets = [(document_features4a(d), c) for (d,c) in documents]
	train_set, test_set = featuresets[100:], featuresets[:100]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)
	classifier.show_most_informative_features(5)


if __name__ == '__main__':
	main()


