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
print("_____________________STATISTICS___________________________")
def mean(x):
    return sum(x)/len(x)
print("Mean: ",mean(tweets_year))
def median(x):
    n = len(x)
    sorting = sorted(x)
    mid = n //2
    if n % 2 == 1:
        return sorting[mid]
    else:
        return (sorting[mid]+sorted[mid]) /2
print("Median: ",median(tweets_year))
def dataRange(x):
	return max(x) - min(x)
print("range: ", dataRange(tweets_year))
def deviated_mean(x):
	x_bar = mean(x)
	return[x_i-x_bar for x_i in x]	
def sumSquares(n):
	return sum([x**2 for x in n])
def variance(x):
	n = len(x)
	deviate = deviated_mean(x)
	return sumSquares(deviate)/(n-1)
print("Variance:", variance(tweets_year))
def standardDeviation(x):
	return math.sqrt(variance(x))
print("standard deviation: ", standardDeviation(stored))

twitterData = Counter(x for x in stored)
print(twitterData)

size = 50
mean1 = mean(stored)
population = standardDeviation(stored) 
print(len(stored))
statistics = stats.norm.ppf(q = 0.05) 
m_o_g = -statistics * (population/math.sqrt(size))
Interval = (mean1 - m_o_g,mean1 + m_o_g)  					   
print("Confidence interval of tweets_year:",Interval)	