# AUTHOR: GIRISH SRINIVAS

import nltk, random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn

featureset1 = []
ss = [i for i in wn.all_synsets()]
for i in range(len(ss)):
	word = ss[i].name.split(".")
	if word[2] == "01":
		featureset1.append(ss[i].lemma_names[0])

lemma_features = set(featureset1)

def document_features8b(document): 
    document_words = set(document) 
    features = {}
    for word in lemma_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def main():
	documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
	random.shuffle(documents)
	featuresets = [(document_features8b(d), c) for (d,c) in documents]
	train_set, test_set = featuresets[100:], featuresets[:100]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)


if __name__ == '__main__':
	main()



