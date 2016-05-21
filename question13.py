# AUTHOR: GIRISH SRINIVAS

import nltk, re, pprint

from nltk.book import *
from nltk.corpus import *
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

def exercise13():
    print
    print "Exercise 13"
    count = 0
    den = 0
    noun = list(wn.all_synsets('n'))
    for w in noun:
        if (len(w.hyponyms()) == 0):
            count = count + 1
    num = float(count)
    den = float(len(noun))
    res = num/den
    print res*100
    print

def main():
    exercise13()


if __name__ == "__main__":
    main()