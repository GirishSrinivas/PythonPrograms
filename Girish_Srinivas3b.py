"""
AUTHORS: GIRISH SRINIVAS
"""
#nltk chapter 3b assignment

from __future__ import division
import nltk, re, pprint

from urllib import urlopen

from nltk.book import *

from nltk.corpus import abc
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def exercise18():
    print
    print "Exercise - 18:"
    pattern_wh1 = r'^wh'
    pattern_wh2 = r'^Wh'
    pattern_wh3 = r'^WH'
    pattern_wh = pattern_wh1 + "|" + pattern_wh2 + "|" + pattern_wh3

    pattern1 = r'^wh(at|y|o|om|ere|en|ich|ose)$'
    pattern2 = r'^Wh(at|y|o|om|ere|en|ich|ose)$'
    pattern3 = r'^WH(AT|Y|O|OM|ERE|EN|ICH|OSE)$'
    pattern = pattern1 + "|" + pattern2 + "|" + pattern3

    words_text2 = sorted(set(text2))
    words_text7 = sorted(set(text7))

    print "For text2"
    print "Displaying result for all 'wh' word types:"
    pattern_text2_wh = [w for w in words_text2 if re.search(pattern_wh, w)]
    print pattern_text2_wh
    print
    print "Displaying result for 'wh' word types for given set:"
    pattern_text2 = [w for w in words_text2 if re.search(pattern, w)]
    print pattern_text2
    print
    print "For text7"
    print "Displaying result for all 'wh' word types:"
    pattern_text7_wh = [w for w in words_text7 if re.search(pattern_wh, w)]
    print pattern_text7_wh
    print
    print "Displaying result for 'wh' word types for given set:"
    pattern_text7 = [w for w in words_text7 if re.search(pattern, w)]
    print pattern_text7
    print


def exercise29():
    print
    print "Exercise - 29:"
    print "Automated_Readability_Index for different categories of Brown Corpus are:"
    sections = brown.categories()
    for section in sections:
        result = Automated_Readability_Index29(section)
        print section + " : %f" %result
    print

def Automated_Readability_Index29(section):
    char_count = 0
    sent = len(brown.sents(categories = section))
    words = len(brown.words(categories = section))
    raw_text = brown.raw(categories = section)

    for ch in raw_text:
        if ch.isalpha():
            char_count = char_count + 1

    uw = char_count / float(words) 
    us = words / float(sent) 
    ARI = (4.71 * uw) + (0.5 * us) - 21.43
    return ARI


def exercise30():
    print
    print "Exercise - 30:"
    porter_stem_words = ""
    lancaster_stem_words = ""
    tokenized_words = nltk.word_tokenize(SimpleText)
    p = nltk.PorterStemmer()
    l = nltk.LancasterStemmer()
    print "Raw text:"
    print SimpleText
    print
    print "Stemming of raw text using PorterStemmer"
    for t in tokenized_words:
        porter_stem_words = porter_stem_words + p.stem(t) + " "

    print porter_stem_words
    print
    print "Stemming of raw text using LancasterStemmer"
    for t in tokenized_words:
        lancaster_stem_words = lancaster_stem_words + l.stem(t) + " "

    print lancaster_stem_words


def exercise40():
    print
    print "Exercise - 40:"
    print "Automated_Readability_Index in ABC Corpus are:"
    fileids = abc.fileids()
    for section in fileids:
        result = Automated_Readability_Index40(section)
        print section + " : %f" %result
    print

def Automated_Readability_Index40(section):
    char_count = 0
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_text = abc.raw(section)
    sent = len(sent_tokenizer.tokenize(raw_text))
    words = len(abc.words(section))
    
    for ch in raw_text:
        if ch.isalpha():
            char_count = char_count + 1
    
    uw = char_count / float(words) 
    us = words / float(sent) 
    ARI = (4.71 * uw) + (0.5 * us) - 21.43
    return ARI


def main():
    exercise18()
    exercise29()
    exercise30()
    exercise40()


if __name__ == "__main__":
    main()

