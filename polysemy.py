# AUTHOR: GIRISH SRINIVAS

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

# The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')). Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.

def polysemy(group):
    polysemy = 0
    count = 0
    name = ''

    for synset in wn.all_synsets(group):
        for lemma in synset.lemmas:
            name = lemma.name
            polysemy = polysemy + len(wn.synsets(name, group))
            count = count + 1

    return polysemy / count

def main():
	noun = polysemy('n')
	verb = polysemy('v')
	adverb = polysemy('r')
	adj = polysemy('a')

	print "Average polysemy of Nouns: %f" % noun
	print "Average polysemy of Verbs: %f" % verb
	print "Average polysemy of adverbs: %f" % adverb
	print "Average polysemy of Adjectives: %f" % adj

if __name__ == "__main__":
    main()