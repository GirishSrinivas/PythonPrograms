import nltk
from nltk.corpus import words

def question4():
	wrds = words.words()
	tag_wrds = nltk.pos_tag(wrds)
	list_tag_wrds = [(w,t) for (w,t) in tag_wrds if t == 'NN' or t == 'VB' or t == 'JJ' or t == 'RB']
	cfd = nltk.ConditionalFreqDist(list_tag_wrds)
	count_pos = 0
	for (w,t) in list_tag_wrds:
		if(len(cfd[w].keys()) > 1):
			count_pos = count_pos + 1

	count_neg = 0
	for (w,t) in list_tag_wrds:
		if (len(cfd[w].keys()) == 1):
			count_neg = count_neg + 1

	total_count = len(list_tag_wrds)
	percentage_pos = (count_pos /float(total_count)) * 100.0
	percentage_neg = (count_neg / float(total_count)) * 100.0

	print count_pos
	print count_neg
	print total_count
	print percentage_pos
	print percentage_neg


def main():
	question4()

if __name__ == '__main__':
	main()