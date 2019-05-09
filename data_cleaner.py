#!/home/marlabs/anaconda3/bin/python
import re
words_to_remove = '-+$#@!_.()[]{}"\\\''
words_to_remove_int = 'n$#@!_()[]{}"\\\'/'

def remove_these_words(text):
	text = text.rstrip("\n\r")
	for i in words_to_remove:
		text = text.replace(i, ' ')
	text = re.sub(' +',' ', text)
	return text.strip().lower()

def clean_number(text):
	text = text.rstrip("\n\r")
	for i in words_to_remove_int:
		text = text.replace(i, ' ')
	text = re.sub(' +',' ', text)
	text = text.strip().lower()
	return float(text) 

def split_words(text):
	return text.split(' ')

def all_ops_on_words(text):
	clean_text = remove_these_words(text)
	return split_words(clean_text)

'''
sample = 'Product arrived labeled as Jumbo Salted Peanuts...the peanuts were actually small sized unsalted. Not sure if this was an error or if the vendor intended to represent the product as "Jumbo".'

print(sample)
print(remove_these_words(sample))
print(split_words(remove_these_words(sample)))

sample = '5.0/n'
print(clean_number(sample))
'''

