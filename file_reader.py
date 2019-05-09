#!/home/marlabs/anaconda3/bin/python
import sys
from pprint import pprint
from data_cleaner import all_ops_on_words, remove_these_words, clean_number
import io

def get_data(filename=None):
	if filename == None:
		filename = 'small.txt'
	gdict = dict()
	count = 1
	with io.open(filename, 'r', encoding='utf-8', errors="ignore") as fp:
		tdict = dict()
		for line in fp.readlines():
			if line == '\n':
				if tdict == dict():
					pass
				else:
					gdict[count] = tdict
					count += 1
					tdict = dict()
			else:
				text = line.rstrip('\n\r')
				text = line.split(': ')
				key = text[0]
				value = ": ".join(text[1:])
				if key == 'review/summary' or key == 'review/text':
					tdict[key] = all_ops_on_words(value)

				elif key == 'review/score':
					tdict[key] = clean_number(value)
				else:
					tdict[key] = remove_these_words(value)
	return gdict	
		
if __name__ == '__main__':
	if len(sys.argv) > 1:
		import cProfile
		cProfile.run(	'get_data(sys.argv[1])')
#pprint(get_data('large.txt'))	
