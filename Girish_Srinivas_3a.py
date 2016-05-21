#AUTHOR: GIRISH SRINIVAS
#DATE: 09 February, 2016

#CSCI-8450-001 ADVANCE NATURAL LANGUAGE UNDERSTANDING
#ASSIGNMENT 3a.

from __future__ import division
import nltk, re, pprint

from urllib import urlopen

from nltk import book

from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

SimpleText='One day, his horse ran away. The neighbors came to express their concern: "Oh, that\'s too bad. How are you going to work the fields now?" The farmer replied: "Good thing, Bad thing, Who knows?" In a few days, his horse came back and brought another horse with her. Now, the neighbors were glad: "Oh, how lucky! Now you can do twice as much work as before!" The farmer replied: "Good thing, Bad thing, Who knows?"'

def exercise6():
    print
    print "Exercise 6"
    print "Part b"
    patternb = r'[A-Z][a-z]*'
    partb = nltk.regexp_tokenize(SimpleText, patternb)
    print "Pattern for regexp - b: ", partb
    print
    print("Part c")
    patternc = r'p[aeiou]{,2}t'
    partc = nltk.regexp_tokenize(SimpleText, patternc)
    print "Pattern for regexp - c: ", partc
    print
    print("Part f")
    patternf = r'\w+|[^\w\s]+'
    partf = nltk.regexp_tokenize(SimpleText, patternf)
    print "Pattern for regexp - f: ", partf
    print


def exercise7():
    print
    print "Exercise 7"
    pattern = r'\bthe\b|\bThe\b|\ba\b|\bA\b|\ban\b|\bAn\b'
    Determiners = nltk.regexp_tokenize(SimpleText, pattern)
    print "Determiners are: ", Determiners
    print



def exercise21():
    print
    print "Exercise 21"

    def unknown(url):
        text = urlopen(url).read()
        sub_string = set(re.findall(r'[a-z]+', text))
        english = set(w.lower() for w in nltk.corpus.words.words())
        all_unusual = sub_string.difference(english)
        print "Words in all_unusual", all_unusual
        print "Length of text: ", len(text)
        print "Length of unusual words for all words in text: " ,len(all_unusual)
        print

        tokens = nltk.word_tokenize(text)
        small_words = set(w.lower() for w in tokens if w.isalpha())
        token_unusual = small_words.difference(english)
        print "Words in token_unusual", token_unusual
        print "Set of tokens", len(tokens)
        print "Length of unusual words for tokens: " ,len(token_unusual)
        print
    
        l = nltk.WordNetLemmatizer()
        wordl = [l.lemmatize(lt) for lt in tokens]
        lemmatized_small_words = set(w.lower() for w in wordl if w.isalpha())
        lemmatized_unusual = lemmatized_small_words.difference(english)
        print "Words in lemmatized_unusual", lemmatized_unusual
        print "lemmatized set of words: ", len(wordl)
        print "Length of unusual words for lemmatized words: " ,len(lemmatized_unusual)
        print

    url = "https://www.cs.utexas.edu/~vl/notes/dijkstra.html"
    unknown(url)
    

def exercise25():
    print
    print "Exercise 25"
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    def convert_word(word):
        for i in range(len(word)):
            for j in range(len(vowels)):
                if word[i] == vowels[j]:
                    return word[i:] + word[:i] + "ay"
                

    def convert_sentence(sentence):
        words = sentence.split()
        converted_sentence = ""
        for word in words:
            converted_sentence = converted_sentence + convert_word(word)
            converted_sentence = converted_sentence + " "
        return converted_sentence

    ip = raw_input("Enter ONLY one word: ")
    print convert_word(ip)
    print "For Sentence(for SimpleText): "
    print convert_sentence(SimpleText)
    print
    

def main():
    exercise6()
    exercise7()
    exercise21()
    exercise25()


if __name__ == "__main__":
    main()

