# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.corpus import brown as bn

brown_news_tagged_sents = bn.tagged_sents(categories = 'news')
brown_lore_tagged_sents = bn.tagged_sents(categories = 'lore')
unigram_tagger = nltk.UnigramTagger(brown_news_tagged_sents)
brown_news_eval = unigram_tagger.evaluate(brown_news_tagged_sents)
brown_lore_eval = unigram_tagger.evaluate(brown_lore_tagged_sents)
print brown_news_eval
print brown_lore_eval
brown_lore = bn.sents(categories = 'lore')
b_lore = unigram_tagger.tag(brown_lore[200])
print b_lore
