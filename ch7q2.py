# AUTHOR: GIRISH SRINIVAS

import nltk

grammar = r"""
	NP: {<DT>?<JJ><NNS>}
		{<CD><NNS>}
"""
cp = nltk.RegexpParser(grammar)
sentenceSample = [("Many", "JJ"), ("little", "JJ"),   ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("cats", "NNS")]
res = cp.parse(sentenceSample)
for r in res.subtrees():
	if r.node == 'NP':
		print r