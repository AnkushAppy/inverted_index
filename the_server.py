#!/home/marlabs/anaconda3/bin/python
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from query_builder import Search
import pprint

app = Flask(__name__)

#filename =  'finefoods.txt'
filename =  'large.txt'
search = Search(filename)
search.fillup()

@app.route('/', methods=['GET'])
def index():
	return 'Great!!'

@app.route('/search', methods=['GET'])
def search_query():
	try:
		q = request.args['query']
	except:
		return 'None'
	results = search.find(q)
	return "****************************************************\n\n\n".join(['text:{}\nsummary:{}'.format(r[0],r[1]) for r in results])


