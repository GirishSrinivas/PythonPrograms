import nltk
from nltk.corpus import wordnet as wn

ctr = 0
als = list(wn.all_synsets('n'))
for w in als:
    if(len(w.hyponyms()) == 0):
        ctr = ctr + 1
print ctr/len(als)