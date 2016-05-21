"""
AUTHORS: GIRISH SRINIVAS
"""

import nltk
import random
from nltk.corpus import names
from nltk.corpus import wordnet as wn
from nltk.corpus import brown as bn
from urllib import urlopen
from nltk.book import *

def exercise1(text):
    print
    print "Exercise - 1"
    result = sum([len(w) for w in text])
    print "Sum of lenght of all words in text3 is: %d" %result
    print "Average word length of 'The book of Genesis' is: %f" %(result/float(len(text)))
    print


def exercise2(text):
    print
    print "Exercise - 2"
    word4 = [w for w in text if len(w) == 4]
    fdist = FreqDist(word4)
    print "The most frequent 4 letter words are:"
    print fdist.keys()[:5]
    print


def exercise3():
    print
    print "Exercise - 3"
    ss = [w for w in wn.all_synsets('v')]
    result = sum([len(ss[i].hypernyms()) for i in range(len(ss))])
    print "Total number of hypernyms of 'v' is: %d" %result
    print "Average number of hypernyms is: %f" %(result/float(len(ss)))


def token_frequency(token, category):
    words = bn.words(categories = category)
    fdist = nltk.FreqDist([w.lower() for w in words])
    freq = fdist.freq(token)
    print "Frequency of the token '%s' in category: '%s' is: %f" %(token ,category, freq)


def exercise4():
    print
    print "Exercise - 4"
    token1 = ';'
    token2 = 'bear'
    print "First token"
    category = ['lore', 'news']
    for c in category:
        token_frequency(token1, c)
    print
    print "Second token"
    category = ['lore', 'news']
    for c in category:
        token_frequency(token2, c)
    print


def stringFunction(string):
    print "Input string is: %s" %string
    print
    bland = string.split()
    print "The split string is: "
    print bland
    print
    secondLetter = ''
    for i in range(len(string)):
        if i == 0:
            secondLetter = secondLetter + string[i + 1]
        if string[i] == ' ':
            secondLetter = secondLetter + string[i + 2]
    print "Every second letter is: %s" %secondLetter
    print
    space = ' '
    newString = space.join(bland)
    print "The joined letters are: %s" %newString
    print
    order = string.split()
    order.sort()
    print "Alphabetical order of the input string is: "
    for i in order:
        print i
    print


def exercise5():
    print
    print "Exercise - 5"
    silly = 'newly formed bland ideas are inexpressible in an infuriating way'
    input2 = 'colorless green ideas sleep furiously'

    stringFunction(silly)
    stringFunction(input2)
    print


def exercise6():
    print
    print "Exercise - 6"
    url = "https://www.clear.rice.edu/comp200/resources/texts/Green%20Eggs%20and%20Ham.txt"
    html = urlopen(url).read()
    raw = nltk.clean_html(html) 
    tokens = nltk.word_tokenize(raw)
    fdist = nltk.FreqDist(tokens)
    highFreqWords = fdist.keys()
    print "The sorted list of words in decending order of their occurances are:"
    for i in range(10):
        print highFreqWords[i] + " -> " + "%d" %fdist[highFreqWords[i]]
    print


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


def exercise7():
    print
    print "Exercise - 7"
    size = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for s in size:
        lookupTagger(s)
    print


name = ([(n, 'male') for n in names.words('male.txt')] + [(n, 'female') for n in names.words('female.txt')])
random.shuffle(name)

def genderFeature1(name):
    return {'last_letter': name[-1]}

def genderFeature2(name):
    return {'length': len(name), 'first_letter': name[0], 'last_2_letters': name[-2:]}


def exercise8():
    print
    print "Exercise - 8"
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
    text1 = text3
    exercise1(text1)

    text2 = text5
    exercise2(text2)

    exercise3()

    exercise4()

    exercise5()

    exercise6()

    exercise7()

    exercise8()


if __name__ == "__main__":
    main()

