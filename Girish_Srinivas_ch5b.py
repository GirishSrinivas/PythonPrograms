from __future__ import division
"""
AUTHORS: GIRISH SRINIVAS
         VAISHNAVI PADAM
"""
import nltk, re, pprint

from nltk.corpus import brown as bn
from nltk.corpus import words

def exercise1():
    print
    print "Exercise 1:"
    brown_news_tagged_sents = bn.tagged_sents(categories = 'news')
    brown_lore_tagged_sents = bn.tagged_sents(categories = 'lore')
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(brown_news_tagged_sents, backoff = t0)
    t2 = nltk.BigramTagger(brown_news_tagged_sents, backoff = t1)
    t3 = nltk.TrigramTagger(brown_news_tagged_sents, backoff  = t2)
    brown_news_eval = t3.evaluate(brown_news_tagged_sents)
    brown_lore_eval = t3.evaluate(brown_lore_tagged_sents)
    print "Evaluation using Backoff tagging on 'News': %f " % brown_news_eval
    print "Evaluation using Backoff tagging on 'Lore': %f " % brown_lore_eval
    brown_lore = bn.sents(categories = 'lore')
    b_lore = t3.tag(brown_lore[200])
    print "Tagged words for 200th sentence of 'Brown' corpus of category 'Lore' is: "
    print b_lore
    print


def exercise2():
    print
    print "Exercise 2:"
    brown_news_tagged_sents = bn.tagged_sents(categories = 'news')
    brown_lore_tagged_sents = bn.tagged_sents(categories = 'lore')
    trigram_tagger = nltk.TrigramTagger(brown_news_tagged_sents)
    brown_news_eval = trigram_tagger.evaluate(brown_news_tagged_sents)
    brown_lore_eval = trigram_tagger.evaluate(brown_lore_tagged_sents)
    print "Evaluation of the trigram tagger on 'News': %f " % brown_news_eval
    print "Evaluation of the trigram tagger on 'Lore': %f " % brown_lore_eval
    print


def exercise3a(category):
    print "For category: " +category
    brown_tagged_words = bn.tagged_words(categories = category)
    brown_words = bn.words(categories = category)
    brown_tagged_plural = set([w for (w, t) in brown_tagged_words if t == 'NNS'])
    freq = nltk.FreqDist(brown_words)
    word_cnt_plural = [(w, freq[w]) for w in brown_tagged_plural]
    print "The Plural nouns are:"
    print word_cnt_plural
    wnl = nltk.WordNetLemmatizer()
    lemma_singular = [wnl.lemmatize(t) for t in brown_tagged_plural]
    print
    print
    print "The Singular nouns are:"
    word_cnt_singular = [(w, freq[w]) for w in lemma_singular]
    print word_cnt_singular
    print
    print


def exercise3b(category):
    print "For category: " +category
    brown_tagged_words = bn.tagged_words(categories = category)
    cfd = nltk.ConditionalFreqDist(brown_tagged_words)
    li = [w for (w,t) in brown_tagged_words]
    wrd_cnt = set([(w, len(cfd[w].keys())) for w in li])
    max = 0
    for(w,c) in wrd_cnt:
        if(c >= max):
            max = c

    print "Maximum number of tags: %d" %max
    word_tag = [w for (w,c) in wrd_cnt if c == max]
    for w in word_tag:
        print w
        print cfd[w].keys()
        print

    print
    print


def exercise3c(category):
    print "For category: " +category
    brown_tag_words = bn.tagged_words(categories = category)
    tag_fd = nltk.FreqDist(t for (w,t) in brown_tag_words)
    print tag_fd.keys()[:10]
    print


def exercise4():
    print
    print "Exercise 4:"
    wrds = words.words()
    tag_wrds = nltk.pos_tag(wrds)
    list_tag_wrds = [(w,t) for (w,t) in tag_wrds if t == 'NN' or t == 'VB' or t == 'JJ' or t == 'RB']
    cfd = nltk.ConditionalFreqDist(list_tag_wrds)
    count_pos = 0
    for (w,t) in list_tag_wrds:
        if(len(cfd[w].keys()) > 1):
            count_pos = count_pos + 1

    count_neg = 0
    for (w,t) in list_tag_wrds:
        if (len(cfd[w].keys()) == 1):
            count_neg = count_neg + 1

    total_count = len(list_tag_wrds)
    percentage_pos = (count_pos /float(total_count)) * 100.0
    percentage_neg = (count_neg / float(total_count)) * 100.0

    print "Percentage of positive case: %f" %percentage_pos
    print "Percentaga of negative case: %f" %percentage_neg
    print


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())


def exercise5(category): 
    print "For category: " +category
    print "The common noun tags are:"
    tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories = category))
    for tag in sorted(tagdict):
        print tag
    print


def main():
    categories = ['humor', 'romance', 'government']

    exercise1()

    exercise2()

    print "Exercise 3a:"
    for c in categories:
        exercise3a(c)

    print "Exercise 3b:"
    for c in categories:
        exercise3b(c)

    print "Exercise 3c:"
    for c in categories:
        exercise3c(c)

    exercise4()

    print "Exercise 5:"
    for c in categories:      
        exercise5(c)


if __name__ == "__main__":
    main()

