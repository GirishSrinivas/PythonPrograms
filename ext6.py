import nltk
from urllib import urlopen

url = "https://www.clear.rice.edu/comp200/resources/texts/Green%20Eggs%20and%20Ham.txt"
html = urlopen(url).read()
raw = nltk.clean_html(html) 
tokens = nltk.word_tokenize(raw)
fdist = nltk.FreqDist(tokens)
highFreqWords = fdist.keys()
print "The sorted list of words in decending order of their occurances are:"
for i in range(10):
	print highFreqWords[i] + " -> " + "%d" %fdist[highFreqWords[i]]
#print len(tokens)
