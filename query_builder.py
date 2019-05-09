#!/home/marlabs/anaconda3/bin/python
from pprint import pprint
from inverted_index import index_docs
import datetime
import json

class Search:

	def __init__(self, filename=None):
		self.inv_ind = None
		self.data = None
		self.N = 10
		self.filename = filename
	
	def fillup(self):
		self.inv_ind, self.data = index_docs(self.filename)

	def fetch_top_keywords(self):
		ll = sorted([[i, len(self.inv_ind[i])] for i in self.inv_ind], key=lambda x:x[1], reverse=True )
		print(ll[:20])
		return " ".join([i[0] for i in ll[:20]])

	def find(self, query):
		query_list = set(query.split(' '))
		k = len(query_list)
		word_to_docs = self.find_all_docs(query_list)
		doc_to_word = self.doc_to_word_converter(word_to_docs)
		list_of_docs = self.make_ranking(doc_to_word, k)
		sorted_docs = self.sort_ranking(list_of_docs)
		return self.get_top_n(sorted_docs)		

	def find_all_docs(self, query_list):
		word_to_docs = dict()
		for word in query_list:
			if word in self.inv_ind:
				word_to_docs[word] = self.inv_ind[word]
		print('-'*10)
		top_doc_words = []
		for word in word_to_docs:
			top_doc_words.append([word, len(word_to_docs[word])])
		print(sorted(top_doc_words, key=lambda x:x[1], reverse=True))
		print('-'*10)
		
		return word_to_docs

	def doc_to_word_converter(self, word_to_docs):
		doc_to_word = dict()
		for word in word_to_docs:
			for doc in word_to_docs[word]:
				if doc in doc_to_word:
					doc_to_word[doc].append(word)
				else:
					doc_to_word[doc] = [word]
		return doc_to_word

	def make_ranking(self, doc_to_word, k):
		list_of_docs = []
		#print(doc_to_word)
		for doc in doc_to_word:
			score = float(len(doc_to_word[doc])/k)
			user_score = self.data[doc]['review/score']
			info = [doc, score, user_score]
			list_of_docs.append(info)
		return list_of_docs
	
	def sort_ranking(self, list_of_docs):
		list_of_docs = sorted(list_of_docs, key=lambda x: (x[1], x[2]))
		return list_of_docs

	def get_top_n(self, list_of_docs):
		return list_of_docs[:self.N]

	def write_to_disk(self):
		import os
		inverted_index = 'inv_ind.json'
		whole_data = 'whole_data.json'
		if os.path.exists(inverted_index):
			pass
		else:
			with open(inverted_index, 'w') as fp:
				json.dump(self.inv_ind, fp)

		if os.path.exists(whole_data):
			pass
		else:
			with open(whole_data, 'w') as fp:
				json.dump(self.data, fp)
		self.inv_ind = None
		self.data = None
	
	def find_with_disk(self, query):
		inverted_index = 'inv_ind.json'
		whole_data = 'whole_data.json'
		with open(inverted_index) as fp:
			self.inv_ind = json.load(fp)

		with open(whole_data) as fp:
			self.data = json.load(fp)
		return self.find(query)

queries = [
	'story food',
	'mad mad world',
	'you looking food'
]
filename = None
import sys

if len(sys.argv) > 1:
	print(sys.argv)
	filename = sys.argv[1]

s1 = datetime.datetime.now()
search = Search(filename)
s2 = datetime.datetime.now()
search.fillup()
s3 = datetime.datetime.now()
print('Fillup done.')
print(s3-s2)
print('number of document: ',  len(search.data))
print('number of words: ',  len(search.inv_ind))
best_text = search.fetch_top_keywords()
print('Top keywords are: ', best_text)
queries.append(best_text)
print('*'*30)

for q in queries:
	print(q)
	s4 = datetime.datetime.now()
	print(search.find(q))
	s5 = datetime.datetime.now()
	print(s5-s4)
	

while True:
	print('Please enter a query: ')
	q = input()
	if len(q.split(' ')) > 10:
		continue
	s4 = datetime.datetime.now()
	print(search.find(q))
	s5 = datetime.datetime.now()
	print(s5-s4)
	
