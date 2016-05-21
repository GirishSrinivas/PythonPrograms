import nltk
from nltk.corpus import wordnet as wn

featureset1 = []
ss = [i for i in wn.all_synsets()]
for i in range(len(ss)):
	word = ss[i].name.split(".")
	if word[2] == "01":
		featureset1.append(ss[i].lemma_names[0])

print len(set(featureset1))