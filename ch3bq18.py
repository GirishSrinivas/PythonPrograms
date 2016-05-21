import nltk, re
from nltk.book import *

words_text7 = list(text7)
words_text2 = list(text2)
print "For text2"
pattern1 = r'^wh(at|y|o|om|ere|en|ich|ose)$'
pattern2 = r'^Wh(at|y|o|om|ere|en|ich|ose)$'
pattern3 = r'^WH(AT|Y|O|OM|ERE|EN|ICH|OSE)$'
pattern = pattern1 + "|" + pattern2 + "|" + pattern3
pattern_text2 = sorted(set([w for w in words_text2 if re.search(pattern, w)]))
print pattern_text2
print
print "For text7"
pattern_text7 = sorted(set([w for w in words_text7 if re.search(pattern, w)]))
print pattern_text7