# AUTHOR: GIRISH SRINIVAS

import nltk
import random
from nltk.corpus import names

def genderFeature(name):
	return {len(name) : name[0]+name[len(name)/2]+name[-1]}

	

def main():
	name = ([(n, 'male') for n in names.words('male.txt')] + [(n, 'female') for n in names.words('female.txt')])
	randomNames = random.shuffle(name)

	featuresets = [(genderFeature(n.lower()), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)

	string = raw_input("Enter a name: ")
	print classifier.classify(genderFeature(string))
	print nltk.classify.accuracy(classifier, test_set)

if __name__ == '__main__':
	main()