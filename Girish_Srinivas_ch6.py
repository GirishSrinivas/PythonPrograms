"""
AUTHORS: GIRISH SRINIVAS
         VAISHNAVI PADAM
"""
import nltk, random
from nltk.corpus import movie_reviews
from nltk.corpus import wordnet as wn
from nltk.corpus import names


name = ([(n, 'male') for n in names.words('male.txt')] + [(n, 'female') for n in names.words('female.txt')])
random.shuffle(name)

def genderFeature1(name):
    return {'last_letter': name[-1]}

def genderFeature2(name):
    return {name[0] : name[-2]}

def genderFeature3(name):
    return {'last_2 letter': name[-2:]}

def genderFeature4(name):
    return {name[int(len(name)/2)] : name[-2:]}

def genderFeature5(name):
    return {len(name) : name[0]+name[int(len(name)/2)]+name[-1]} 
    #return {'suffix1': name[-1:], 'suffix2': name[-2:]}

def NaiveBayesClassifier(string):
    print "Naive Bayes Classifier"
    print "Feature - 1:"
    featuresets = [(genderFeature1(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(genderFeature1(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 2:"
    featuresets = [(genderFeature2(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(genderFeature2(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 3:"
    featuresets = [(genderFeature3(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(genderFeature3(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 4:"
    featuresets = [(genderFeature4(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(genderFeature4(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 5:"
    featuresets = [(genderFeature5(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(genderFeature5(string))
    print nltk.classify.accuracy(classifier, test_set)
    print



def DecisionTreeClassifier(string):
    print "Decision Tree Classifier"
    print "Feature - 1:"
    featuresets = [(genderFeature1(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print classifier.classify(genderFeature1(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 2:"
    featuresets = [(genderFeature2(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print classifier.classify(genderFeature2(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 3:"
    featuresets = [(genderFeature3(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print classifier.classify(genderFeature3(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 4:"
    featuresets = [(genderFeature4(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print classifier.classify(genderFeature4(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 5:"
    featuresets = [(genderFeature5(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.DecisionTreeClassifier.train(train_set)
    print classifier.classify(genderFeature5(string))
    print nltk.classify.accuracy(classifier, test_set)
    print


def MaxEntClassifier(string):
    print "Maximum Entropy Classifier"
    print "Feature - 1:"
    featuresets = [(genderFeature1(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.MaxentClassifier.train(train_set)
    print classifier.classify(genderFeature1(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 2:"
    featuresets = [(genderFeature2(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.MaxentClassifier.train(train_set)
    print classifier.classify(genderFeature2(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 3:"
    featuresets = [(genderFeature3(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.MaxentClassifier.train(train_set)
    print classifier.classify(genderFeature3(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 4:"
    featuresets = [(genderFeature4(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.MaxentClassifier.train(train_set)
    print classifier.classify(genderFeature4(string))
    print nltk.classify.accuracy(classifier, test_set)
    print
    print "Feature - 5:"
    featuresets = [(genderFeature5(n), g) for (n, g) in name]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.MaxentClassifier.train(train_set)
    print classifier.classify(genderFeature5(string))
    print nltk.classify.accuracy(classifier, test_set)
    print


def exercise2():
    print "Exercise - 2"
    string = raw_input("Enter a name: ")
    NaiveBayesClassifier(string)
    DecisionTreeClassifier(string)
    MaxEntClassifier(string)


all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000] 

def document_features(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def exercise4():
    print "Exercise - 4"
    documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print "30 features that the classifier finds to be most informative"
    classifier.show_most_informative_features(30)


posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features


def exercise7():
    print "Exercise - 7"
    string = raw_input("Enter a sentence: ") 
    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(dialogue_act_features(string))
    print nltk.classify.accuracy(classifier, test_set)


def document_features8a(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
        if len(wn.synsets(word)) > 0:
            features['contains(%s)' % word] = 'KNOWN'
        else:
            features['contains(%s)' % word] = 'UNK'
    return features


def exercise8a():
    print "Exercise - 8a"
    documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    featuresets = [(document_features8a(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(5)



featureset1 = []
ss = [i for i in wn.all_synsets()]
for i in range(len(ss)):
    word = ss[i].name.split(".")
    if word[2] == "01":
        featureset1.append(ss[i].lemma_names[0])

lemma_features = set(featureset1)

def document_features8b(document): 
    document_words = set(document) 
    features = {}
    for word in lemma_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def exercise8b():
    print "Exercise - 8b"
    documents = [(list(movie_reviews.words(fileid)),category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    featuresets = [(document_features8b(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)


def main():
    exercise2()
    exercise4()
    exercise7()
    exercise8a()
    exercise8b()


if __name__ == "__main__":
    main()

