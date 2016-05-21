"""AUTHORS: GIRISH SRINIVAS
            VAISHNAVI PADAM
"""
#nltk Chapter-2 Assignment

import nltk, re, pprint

from nltk.book import *
from nltk.corpus import *
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn


def exercise2():
    print
    print "Exercise 2"
    words = gutenberg.words('austen-persuasion.txt')
    print "Number of word tokens in the text austen-persuasion.txt: %d" %len(words)
    print "Number of word-types in the text austen-persuasion.txt: %d" %len(set(words))
    print sorted(set(words))
    print


def exercise5():
    print
    print "Exercise 5"
    print "For Bicycle, wheel"
    print "part_meronyms: ", wn.synset('bicycle.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('bicycle.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('bicycle.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('bicycle.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('bicycle.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('bicycle.n.01').substance_holonyms()
    print
    print "For Pen, nib"
    print "part_meronyms: ", wn.synset('pen.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('pen.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('pen.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('pen.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('pen.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('pen.n.01').substance_holonyms()
    print
    print "For Fish, fin"
    print "part_meronyms: ", wn.synset('fish.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('fish.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('fish.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('fish.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('fish.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('fish.n.01').substance_holonyms()
    print
    print "For Window, glass"
    print "part_meronyms: ", wn.synset('window.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('window.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('window.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('window.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('window.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('window.n.01').substance_holonyms()
    print
    print "For Laptop, touchpad"
    print "part_meronyms: ", wn.synset('laptop.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('laptop.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('laptop.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('laptop.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('laptop.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('laptop.n.01').substance_holonyms()
    print
    print "For Car, steering"
    print "part_meronyms: ", wn.synset('car.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('car.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('car.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('car.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('car.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('car.n.01').substance_holonyms()
    print
    print "For Chair, legs"
    print "part_meronyms: ", wn.synset('chair.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('chair.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('chair.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('chair.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('chair.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('chair.n.01').substance_holonyms()
    print
    print "For Book, pages"
    print "part_meronyms: ", wn.synset('book.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('book.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('book.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('book.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('book.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('book.n.01').substance_holonyms()
    print
    print "For Telephone, mic"
    print "part_meronyms: ", wn.synset('telephone.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('telephone.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('telephone.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('telephone.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('telephone.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('telephone.n.01').substance_holonyms()
    print
    print "For Bird, wings"
    print "part_meronyms: ", wn.synset('bird.n.01').part_meronyms()
    print "substance_meronyms: ", wn.synset('bird.n.01').substance_meronyms()
    print "member_meronyms: ", wn.synset('bird.n.01').member_meronyms()
    print "member_holonyms: ", wn.synset('bird.n.01').member_holonyms()
    print "part_holonyms: ", wn.synset('bird.n.01').part_holonyms()
    print "substance_holonyms: ", wn.synset('bird.n.01').substance_holonyms()
    print


def exercise9():
    print
    print "Exercise 9"
    print "Total number of words(Vocabulary) in 'text-1': %d" %len(text1)
    print "Total number of words(Vocabulary) in 'text-7': %d" %len(text7)
    
    if len(text1) > len(text7):
        print "Text 1 has more words"
    else:
        print "Text 7 has more words"

    print "Total number of Distinct Words in 'text-1': %d" %len(set(text1))
    print "Total number of Distinct Words in 'text-7': %d" %len(set(text7))
    if len(set(text1)) > len(set(text7)):
        print "Text 1 is rich in Vocabulary"
    else:
        print "Text 7 is rich in Vocabulary"

    print "Finding Different meaning for the word 'wall'"
    print "Text - 1:"
    text1.concordance("wall")
    print
    print "Text - 7:"
    text7.concordance("wall")
    print
    print "Finding Different meaning for the word 'trial'"
    print "Text - 1:"
    text1.concordance("trial")
    print
    print "Text - 7:"
    text7.concordance("trial")
    print
    print "Finding Different meaning for the word 'lead'"
    print "Text - 1:"
    text1.concordance("lead")
    print
    print "Text - 7:"
    text7.concordance("lead")
    print
    print


def exercise11():
    print
    print "Exercise 11"
    cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
    genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
    modal_verb = ['shall', 'should', 'may', 'had', 'have']
    print "Tabulation data for closed class of words in english"
    print "For modal verbs:"
    cfd.tabulate(conditions = genres, samples = modal_verb)
    print
    print "For Prepositions:"
    prepositions = ['for', 'from', 'onto', 'to', 'with']
    cfd.tabulate(conditions = genres, samples = prepositions)
    print
    print "For Pronoun:"
    pronoun = ['me', 'she', 'her', 'I', 'we']
    cfd.tabulate(conditions = genres, samples = pronoun)
    print


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
    print "Percentage of noun synsets with no hyponyms is: ", res*100
    print


def exercise18():
    print
    print "Exercise 18"
    text = nltk.corpus.brown.words('ca01')
    content = [w for w in text if w.lower() not in stopwords.words('english')]
    onlywords = [n.lower() for n in content if n.isalpha()]
    freq_words = nltk.FreqDist(nltk.bigrams(onlywords))
    vocabulary = freq_words.keys()
    print vocabulary[:50]
    print
 

def exercise27():
    print
    print "Exercise 27"
    noun = poly('n')
    verb = poly('v')
    adverb = poly('r')
    adj = poly('a')

    print "Average polysemy of Nouns: ", noun
    print "Average polysemy of Verbs: ", verb
    print "Average polysemy of adverbs: ", adverb
    print "Average polysemy of Adjectives: ", adj
    print


def poly(ps):
    poly_semy = 0
    count = 0
    name = ''

    for synset in wn.all_synsets(ps):
        for lemma in synset.lemmas:
            names = lemma.name
            poly_semy = poly_semy + len(wn.synsets(names, ps))
            count = count + 1

    return (poly_semy / float(count))


def main():
    exercise2()
    exercise5()
    exercise9()
    exercise11()
    exercise13()
    exercise18()
    exercise27()


if __name__ == "__main__":
    main()

