# AUTHOR: GIRISH SRINIVAS

import nltk, random
from nltk.corpus import movie_reviews

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000] 

def document_features(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def main():
	documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
	random.shuffle(documents)
	featuresets = [(document_features(d), c) for (d,c) in documents]
	train_set, test_set = featuresets[100:], featuresets[:100]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)
	print "30 features that the classifier finds to be most informative"
	classifier.show_most_informative_features(30)


if __name__ == '__main__':
	main()


