from __future__ import division
from collections import Counter
import math, random, csv, json
import os
import ast
from bs4 import BeautifulSoup
import requests
import datetime
import math
import scipy.stats as stats
from matplotlib import pyplot as plt
from collections import Counter

ftweets = []
tweets_file = []

def read_ftweets():
	with open(os.path.expanduser("~\Desktop\saveTweets.txt"), 'r' , encoding= 'ISO-8859-1') as f:
		for line in f:
			ftweets.append(line)

def convert_ftweets_to_dict():
	for i in range(0, len(ftweets)):
		tweets_file.append(ast.literal_eval(ftweets[i]))

def years(x):
	return [created(x[extracted]['user']['created_at']) for extracted in range(0,len(x))]
	
def created(date):
	created = datetime.datetime(datetime.datetime.strptime(date,"%a %b %d %H:%M:%S %z %Y").year,0,0)
	return (created).year	
	
read_ftweets()
convert_ftweets_to_dict()
stored = createdYear(tweets_file)