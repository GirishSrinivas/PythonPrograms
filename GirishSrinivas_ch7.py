"""
AUTHORS: GIRISH SRINIVAS
"""

import nltk, re, pprint
from nltk.corpus import conll2000


def exercise2():
    print "Exercise - 2"
    grammar = r"""
    NP: {<DT>?<JJ><NNS>}
        {<CD><NNS>}
    """
    cp = nltk.RegexpParser(grammar)
    sentenceSample = [("Many", "JJ"), ("little", "JJ"),   ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("cats", "NNS")]
    res = cp.parse(sentenceSample)
    print res
    print


def exercise3():
    print "Exercise - 3"
    grammar1 = r"""
    NP: {<DT>?<JJ><NNS>}
        {<CD><NNS>}
    """
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])[:100]
    cp1 = nltk.RegexpParser(grammar1)
    res1 = cp1.evaluate(test_sents)
    print "Statistics data for custom chunker"
    print res1
    print


    cp2 = nltk.RegexpParser("")
    res2 = cp2.evaluate(test_sents)
    print "Statistics data for baseline chunker"
    print res2
    print

    grammar3 = r"""
    NP: {<DT>?<JJ><NNS>}
        {<CD><NNS>}
        {<DT><NN>}
    """
    cp3 = nltk.RegexpParser(grammar3)
    res3 = cp3.evaluate(test_sents)
    print "Statistics data for custom chunker with added regular expression: {<DT><NN>}"
    print res3
    print




def main():
    exercise2()
    exercise3()


if __name__ == "__main__":
    main()

