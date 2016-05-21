import nltk
from nltk.corpus import brown as bn

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
    brown_lore = bn.sents(categories = 'lore')
    b_lore = trigram_tagger.tag(brown_lore[200])
    print "Tagged words for 200th sentence of 'Brown' corpus of category 'Lore' is: "
    print b_lore
    print


def main():
    exercise2()


if __name__ == '__main__':
    main()