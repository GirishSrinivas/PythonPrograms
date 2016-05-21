import nltk, re, pprint

from nltk.book import *
from nltk.corpus import *
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['shall', 'should', 'may', 'had', 'have']
cfd.tabulate(conditions=genres, samples=modals)