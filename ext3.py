# AUTHOR: GIRISH SRINIVAS

import nltk
from nltk.corpus import wordnet as wn

def averageHypernyms():
	ss = [w for w in wn.all_synsets('v')]
	result = sum([len(ss[i].hypernyms()) for i in range(len(ss))])
	print "Total number of hypernyms of 'v' is: %d" %result
	print "Average number of hypernyms is: %f" %(result/float(len(ss)))


def main():
	averageHypernyms()


if __name__ == '__main__':
	main()