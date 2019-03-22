from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request, source='new-scientist'):
	apikey = '832f79aa393c48ccb4804b23a05f8d6d'
	# source= 'new-scientist'

	url = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(source,apikey)

	handle = urllib.request.urlopen(url)
	string = handle.read().decode()
	data= json.loads(string)
	handle.close()
	context= {'newsapi': data}
	return render(request,'news/index.html',context)