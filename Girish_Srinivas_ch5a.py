"""
AUTHORS: GIRISH SRINIVAS
         VAISHNAVI PADAM
"""

#REFERENCE LINK:
"""
Here for our program, we have used the reference for Parts of Speech Tag-set
from the website: http://www.comp.leeds.ac.uk/amalgam/tagsets/upenn.html
"""

import nltk, re, pprint
from nltk.corpus import brown as bn

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'


def exercise1():
    print
    print "Exercise 1:"
    brown_news_tagged_sents = bn.tagged_sents(categories = 'news')
    brown_lore_tagged_sents = bn.tagged_sents(categories = 'lore')
    unigram_tagger = nltk.UnigramTagger(brown_news_tagged_sents)
    brown_news_eval = unigram_tagger.evaluate(brown_news_tagged_sents)
    brown_lore_eval = unigram_tagger.evaluate(brown_lore_tagged_sents)
    print "Evaluation of the unigram tagger on 'News': %f " % brown_news_eval
    print "Evaluation of the unigram tagger on 'Lore': %f " % brown_lore_eval
    brown_lore = bn.sents(categories = 'lore')
    b_lore = unigram_tagger.tag(brown_lore[200])
    print "Tagged words for 200th sentence of 'Brown' corpus of category 'Lore' is: "
    print b_lore
    print


def exercise2(category):
    print
    print "For Category: " + category
    print "Part 1"
    print "Words with the tag 'JJ':"
    words = bn.tagged_words(categories = category)
    wordlist = bn.words(categories = category)
    words_JJ = set(sorted([(word, tag) for (word, tag) in words if tag == 'JJ']))
    print len(words_JJ)
    print
    print "Part 2"
    print "Words with tags 'VBZ' -> 3rd Person Singular Verbs or ('NNPS' or 'NNS') -> plural nouns:"
    words_VBP_NNPS_NNS = [(word, tag) for (word, tag) in words if tag == 'VBZ' or tag == 'NNPS' or tag == 'NNS']
    print words_VBP_NNPS_NNS[:10]
    print
    sent = ""
    print "Part 3"
    print "The 3 most frequent 3-word prepositional phrases are:"
    words = bn.tagged_words(categories = category)
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(words):
        if(t1.startswith('IN') and t2.startswith('AT') and t3.startswith('NN')):
            sent = sent + w1.lower() + " " + w2.lower() + " " + w3.lower() + "."
    sent_part = sent.split(".")
    fd = nltk.FreqDist(sent_part)
    v = fd.most_common(3)
    print v
    print
    print "Part 4"
    print "Ratio of Masculine to Feminine is:"
    male_pattern = r'\bhe\b|\bhis\b|\bhim\b|\bhimself\b'
    female_pattern = r'\bshe\b|\bher\b|\bhers\b|\bherself\b'
    male_pronouns = len([w for w in wordlist if re.search(male_pattern, w.lower())])
    female_pronouns = len([w for w in wordlist if re.search(female_pattern, w.lower())])
    print "Male : Female is -> %d : %d" %(male_pronouns, female_pronouns)
    print

def exercise3():
    print
    print "Exercise 3"
    print "Part 1"
    count = 0
    total_brown_tagged_words = bn.tagged_words()
    cfd1 = nltk.ConditionalFreqDist(total_brown_tagged_words)
    set1 = set([a for (a, b) in total_brown_tagged_words])
    for s in set1:
        if(len(cfd1[s].keys()) == 5):
            count = count + 1

    print "Number of words which have exactly 5 different tags: %d" % count
    print

    print "Part 2"
    print "Words which have the most distinct tags are: "
    tags = [b for (a, b) in bn.tagged_words()]
    fd = nltk.FreqDist(tags)
    ft = fd.keys()
    cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in bn.tagged_words())

    for a in ft:
        if fd[a] == 1:
            print "For POS: " +a
            print cfd2[a].keys()
            print

    print


def main():

    exercise1()

    print "Exercise 2"
    categories = ['humor', 'romance', 'government']
    for c in categories:
        exercise2(c)

    exercise3()


if __name__ == "__main__":
    main()

