import nltk
import random
from nltk.corpus import names

name = ([(n, 'male') for n in names.words('male.txt')] + [(n, 'female') for n in names.words('female.txt')])
random.shuffle(name)

def genderFeature1(name):
	return {'last_letter': name[-1]}

def genderFeature2(name):
	return {'length': len(name), 'first_letter': name[0], 'last_2_letters': name[-2:]}


def NaiveBayesClassifier():
	print "Naive Bayes Classifier"
	print "Feature - 1: -> last_letter"
	featuresets = [(genderFeature1(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 2: -> Length : first_letter : last_2_letters"
	featuresets = [(genderFeature2(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print nltk.classify.accuracy(classifier, test_set)
	print


def main():
	NaiveBayesClassifier()


if __name__ == '__main__':
	main()