import nltk

posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
	features = {}
	for word in nltk.word_tokenize(post):
		features['contains(%s)' % word.lower()] = True
	return features


def main():
	string = raw_input("Enter a sentence: ") 
	featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
	size = int(len(featuresets) * 0.1)
	train_set, test_set = featuresets[size:], featuresets[:size]
	classifier = nltk.NaiveBayesClassifier.train(train_set)
	print classifier.classify(dialogue_act_features(string))
	print nltk.classify.accuracy(classifier, test_set)

if __name__ == '__main__':
	main()