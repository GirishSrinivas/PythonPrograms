import nltk
from nltk.corpus import brown as bn

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

def main():
	exercise1()


if __name__ == "__main__":
    main()