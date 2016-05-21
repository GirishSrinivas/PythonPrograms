# AUTHOR: GIRISH SRINIVAS

import nltk
import random
from nltk.corpus import names

name = ([(n, 'male') for n in names.words('male.txt')] + [(n, 'female') for n in names.words('female.txt')])
random.shuffle(name)

def genderFeature1(name):
	return {'last_letter': name[-1]}

def genderFeature2(name):
	return {name[0] : name[-2]}

def genderFeature3(name):
	return {'last_2 letter': name[-2:]}

def genderFeature4(name):
	return {name[len(name)/2] : name[-2:]}

def genderFeature5(name):
	return {len(name) : name[0]+name[len(name)/2]+name[-1]}	
	#return {'suffix1': name[-1:], 'suffix2': name[-2:]}

def NaiveBayesClassifier():
	print "Naive Bayes Classifier"
	print "Feature - 1:"
	featuresets = [(genderFeature1(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print classifier.classify(genderFeature1(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 2:"
	featuresets = [(genderFeature2(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print classifier.classify(genderFeature2(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 3:"
	featuresets = [(genderFeature3(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print classifier.classify(genderFeature3(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 4:"
	featuresets = [(genderFeature4(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print classifier.classify(genderFeature4(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 5:"
	featuresets = [(genderFeature5(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	#print classifier.classify(genderFeature5(string))
	print nltk.classify.accuracy(classifier, test_set)
	print



def DecisionTreeClassifier():
	print "Decision Tree Classifier"
	print "Feature - 1:"
	featuresets = [(genderFeature1(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.DecisionTreeClassifier.train(train_set)
	#print classifier.classify(genderFeature1(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 2:"
	featuresets = [(genderFeature2(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.DecisionTreeClassifier.train(train_set)
	#print classifier.classify(genderFeature2(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 3:"
	featuresets = [(genderFeature3(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.DecisionTreeClassifier.train(train_set)
	#print classifier.classify(genderFeature3(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 4:"
	featuresets = [(genderFeature4(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.DecisionTreeClassifier.train(train_set)
	#print classifier.classify(genderFeature4(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 5:"
	featuresets = [(genderFeature5(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.DecisionTreeClassifier.train(train_set)
	#print classifier.classify(genderFeature5(string))
	print nltk.classify.accuracy(classifier, test_set)
	print


def MaxEntClassifier():
	print "Maximum Entropy Classifier"
	print "Feature - 1:"
	featuresets = [(genderFeature1(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.MaxentClassifier.train(train_set)
	#print classifier.classify(genderFeature1(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 2:"
	featuresets = [(genderFeature2(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.MaxentClassifier.train(train_set)
	#print classifier.classify(genderFeature2(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 3:"
	featuresets = [(genderFeature3(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.MaxentClassifier.train(train_set)
	#print classifier.classify(genderFeature3(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 4:"
	featuresets = [(genderFeature4(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.MaxentClassifier.train(train_set)
	#print classifier.classify(genderFeature4(string))
	print nltk.classify.accuracy(classifier, test_set)
	print
	print "Feature - 5:"
	featuresets = [(genderFeature5(n), g) for (n, g) in name]
	train_set, test_set = featuresets[500:], featuresets[:500]
	classifier = nltk.MaxentClassifier.train(train_set)
	#print classifier.classify(genderFeature5(string))
	print nltk.classify.accuracy(classifier, test_set)
	print

def main():
	#string = raw_input("Enter a name: ")
	NaiveBayesClassifier()
	DecisionTreeClassifier()
	MaxEntClassifier()




if __name__ == '__main__':
	main()