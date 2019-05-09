#!/home/marlabs/anaconda3/bin/python
from file_reader import get_data
from pprint import pprint

def index_word(word, doc_id, inv_ind):
	if word in inv_ind:
		inv_ind[word].append(doc_id)
	else:
		inv_ind[word] = [doc_id] 

def index_doc(doc_id, doc, inv_ind):
	#pprint(doc)
	summary_words = doc['review/summary']
	text_words = doc['review/text']
	all_words = summary_words + text_words
	all_words = set(all_words)
	for word in all_words:
		index_word(word, doc_id, inv_ind)

def index_docs(filename=None):	
	data = get_data(filename)
	inv_ind = dict()

	for key in data:
		index_doc(key, data[key], inv_ind)

	return inv_ind, data

#pprint(index_docs())
