import nltk
from nltk.corpus import abc

def Automated_Readability_Index40(section):
	sent_tokenize = nltk.data.load('tokenizers/punkt/english.pickle')
	text = abc.raw(section)
	sents = len(sent_tokenize.tokenize(text))
	words = len(abc.words(section))
	text = " ".join(abc.words(section))
	letters = len(text)
	uw = letters / float(words) 
	us = words / float(sents) 
	ari = (4.71 * uw) + (0.5 * us) - 21.43
	return ari

def main():
	for section in abc.fileids():
		print section + " : %f" %Automated_Readability_Index40(section)

if __name__ == "__main__":
    main()


