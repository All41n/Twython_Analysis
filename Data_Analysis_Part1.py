import numpy as np
from matplotlib import pyplot as plt
import re
import pandas as pd
from collections import Counter
import scipy.stats as stats
import math


Type = ["medical","fashion","electrical","government","Property","funiture","educational","jewellery","jewellery","medical","fashion","fashion","fashion","fashion","medical","fashion","jewellery","government","government","electrical","educational","electrical","electrical","fashion","funiture","electrical","Property","electrical","fashion","fashion","fashion","electrical","funiture","medical","jewellery","educational","fashion","supermarket","jewellery","fashion","educational","fashion","supermarket","fashion","book","medical","supermarket","fashion","book","gaming","sports equipment","fashion","gaming","gaming","government","funiture","medical","electrical","educational","gaming","Property","book","fashion","fashion","jewellery","medical","government","Property","fashion","gaming","fashion","educational","Property","fashion","fashion","educational","sports equipment","gaming","educational","gaming","sports equipment","electrical","fashion","fashion","jewellery","Property","sports equipment","educational","medical","supermarket","book","electrical","Property","sports equipment","educational","electrical","fashion","fashion","fashion","educational"]

no_of_live_days = [502,189,76,518,423,234,155,543,1009,321,176,298,50,256,33,200,653,86,180,321,176,298,50,256,33,76,484,111,762,154,600,965,175,96,321,145,189,7,514,654,980,136,79,865,973,145,335,75,34,28,168,94,54,3,100000,264,433,42,354,87,522,1143,56,438,9,321,176,298,50,256,33,632,976,58,164,76,54,321,87,609,99,172,743,465,23,2,77,91,76,83,143,532,176,996,436,78,185,365,909,307]

down_time=[80.3,51.2,27.3,64.3,75.4,5.1,31.4,64.2,101.3,61.3,24.5,43.8,0.5,31.42,1.3,18,126.8,4.7,13.2,47.1,12.2,41.5,0.3,31.4,1.1,4.1,86.2,3.2,152.9,6.9,114,201.6,12,2.9,47.1,4.8,3.2,2.9,93.4,126.9,205.2,3.64,5.1,177.6,203.52,4.8,1020,3.2,0,0,10.32,0.6,1,0,56.1,33,73.9,0.8,54.9,10.7,95.28,244.32,0.3,75.12,9,47,12.24,41.52,8,31.44,0.6,121.7,204.24,5.3,10.8,5.7,3.4,23.1,2,116.2,5.3,11.3,148.3,81.6,3.3,0,34.1,4.5,31.6,21.6,4.3,91.2,8,212,75,9,14.4,57.6,188.2,43.7]

no_of_hits = [3000,12663,4921,34798,28341,11678,10890,56785,57609,21507,51792,29966,3350,17131,2221,13454,43789,6000
,12067,21507,11792,19966,350,7152,2211,4311,124280,7437,51054,10318,40200,54444,275,6431,21509,1009,5963,4489,34438
,43818,65660,9112,5293,57955,65191,8767,22441,5025,2278,1876,11256,6298,3618,201,567,17688,29011,2678,23576,5892,34974
,345,3752,29346,609,21507,11792,10099,3350,17152,2211,42344,76543,3886,10966,"NA",3651,21560,5878,40890,6632,11456,49879
,31145,1541,134,5159,6097,5092,5561,9581,356,11798,66732,29212,5226,12000,2456,"NA",3233]


still_alive= ["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","no","yes","yes","yes","no","yes","yes","yes","yes"]

no_of_sales = [3960,886,1273,4176,3400,1401,762,8919,23043,5376,3625,1397,1340,2056,555,1608,420,720,4827,2580,2948,1397,42,858,265,1724.4,"NA",892,3573,1238,30150,6534,33,450,2581,403,1490,538.68,2410,32864,2000,3644,635,6954,7823,6575,1571,603,200,1350,756,6000,434,175,381,23000,21700,187,321,28929,0,4199,3700,7337,3522,"NA",0,156,402,"NA",884,296,0,272,1315,23,256,16170,4408,4907,798,1374,3481,3737,20003,0,619,427,1273,667,24,2,0,7689,7303,1306,840,172,8700,388]



average_sales_value = [15.67,19.99,398.1,1298.76,567.5,676.5,5.5,23.56,578.15,14.8,250.17,40.8,45.9,30.5,25.7,1056.89,75.5,50.9,77.5,156.9,300.1,98.5,567.14,23.6,256.75,276.75,0,176.5,23.84,124.5,673,1890,25000,32,75.9,15.99,324.7,45.67,129.99,98.1,150.99,67.5,76.5,43.6,23.56,78.15,14.8,250.17,30.8,45.9,1300.5,25.7,256.89,25.5,19.99,345,54.1,231,45,76.3,0,45.5,67.1,198.8,35.6,25.2,0,435,45,"NA",87.34,24,0,67,23.4,550,1345.87,33.3,23.4,92.1,499.99,56.5,67.8,34.2,234.4,0,155.42,78.9,50.5,141.3,54.67,4230.12,0,287,25,643,25,154.98,543.15,50]

average_user_age=[56,27,45,54,25,46,50,32,46,54,33,23,20,24,37,51,25,48,49,
33,43,47,53,19,31,26,43,23,22,22,38,43,34,19,33,39,41,35,22,24,25,28,56,65,46,
55,20,29,18,23,20,18,37,51,25,43,49,68,23,45,31,52,23,43,53,78,39,51,32,54,
23,38,58,31,21,22,27,43,42,53,23,33,23,20,19,37,51,25,43,49,33,43,42,53,43,56,183,19,31,5]


usability_rating = [1,2,2,4,1,2,3,3,4,4,2,4,3,2,4,2,2,2,3,3,2,1,2,1,2,3,3,2,4,1,2,
3,1,1,2,1,3,1,2,4,1,4,2,3,2,4,1,4,2,4,3,3,2,3,3,4,4,1,1,4,4,2,4,3,
4,3,2,1,4,3,2,1,4,3,1,2,4,4,1,3,3,3,3,3,2,4,1,2,3,3,2,3,1,4,2,2,1,2,3,1]

#Handling Missing Data from List
#To handle the missing data from the lists, an iteration was needed to remove what was not an integer
noh_missingData = [z for z in no_of_hits if type(z) ==int]
nos_missingData = [z for z in no_of_sales if type(z) ==int]
avsv_missingData = [z for z in average_sales_value if type(z) ==int]

def getMean(x):
	mean = sum(x)/len(x)
	return mean
print("MEAN")
print("down_time: ",getMean(down_time))
print("average_user_age: ",getMean(average_user_age))
print("usability_rating: ",getMean(usability_rating))
print("no_of_live_days: ",getMean(no_of_live_days))
print("nos_missingData: ",getMean(nos_missingData))
print("noh_missingData: ",getMean(noh_missingData))
print("avsv_missingData: ",getMean(avsv_missingData))
print("______________________________________________________________")
# def nonNumeric(x):
	# invalid = re.compile('[^0-9]')
	# cleaned = [x for x in no_of_hits if x.isdigit()]
	# print(cleaned)
	
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
print("MEDIAN")
print("average_user_age: ",median(average_user_age))
print("usability_rating: ",median(usability_rating))
print("down_time: ",median(down_time))
print("no_of_live_days: ",median(no_of_live_days))
print("no_of_hits: ",median(noh_missingData))
print("no_of_sales: ",median(nos_missingData))
print("average_sales_value: ",median(avsv_missingData))

def dataRange(x):
	return max(x) - min(x)
print("range of no_of_live_days: ", dataRange(no_of_live_days))
print("range of down_time: ", dataRange(down_time))
print("range of nos_missingData: ", dataRange(nos_missingData))
print("range of noh_missingData: ", dataRange(noh_missingData))
print("range of avsv_missingData: ", dataRange(avsv_missingData))
print("range of average_user_age: ", dataRange(average_user_age))
print("range of usability_rating: ", dataRange(usability_rating))

print("______________________________________________________________")
def variance(x):
	v = sum(x)/len(x)
	varRes = sum([(x1 - v)**2 for x1 in x])/len(x)
	return varRes

print("VARIANCE")
print("average_user_age: ",variance(average_user_age))
print("usability_rating: ",variance(usability_rating))
print("down_time: ",variance(down_time))
print("no_of_hits: ",variance(noh_missingData))
print("no_of_sales: ",variance(nos_missingData))
print("average_sales_value: ",variance(avsv_missingData))

def standardDeviation(x):
	return math.sqrt(variance(x))
print("standard deviation of no_of_live_days = ", standardDeviation(no_of_live_days))
print("standard deviation of down_time = ", standardDeviation(down_time))
print("standard deviation of the no_of_hits  = ",standardDeviation(noh_missingData))
print("standard deviation of the no_of_sales  = ",standardDeviation(nos_missingData))
print("standard deviation of the average_sales_value  = ",standardDeviation(avsv_missingData))
print("standard deviation of the average_user_age  = ",standardDeviation(average_user_age))
print("standard deviation of the usability_rating  = ",standardDeviation(usability_rating))
print("______________________________________________________________")
def covariance(x,y):
	x_mean = getMean(x)
	y_mean = getMean(y)
	data = [(x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))]
	return sum(data)/(len(data)-1)
	
print("Covariance")
print(covariance(average_user_age,usability_rating))
print("______________________________________________________________")
def sd(a):
    return math.sqrt(sum([i*i for i in a])-len(a)*getMean(a)**2)
print("______________________________________________________________")
def pearsonCorrelation(x,y):
    s_x = sd(x)
    s_y = sd(y)
    sum_xy = sum([x*y for x,y in zip(x,y)])
    x_mean = getMean(x)
    y_mean = getMean(y)
    n = len(x)
    return (sum_xy-n*x_mean*y_mean)/(s_x*s_y)
	
print("Correlation: ", pearsonCorrelation(no_of_live_days,down_time))
def b0(x,y):
	return getMean(y) - b1(x,y)*getMean(x)
	
def b1(x,y):
	return (sd(y)/sd(x))*pearsonCorrelation(x,y)


def linear_Regression(m,c,x):
    y=m*x+c
    return y

b_1 = b1(no_of_live_days,down_time)
b_0 = b0(no_of_live_days,down_time)

predictedResults = [linear_Regression(b_1,b_0,x) for x in no_of_live_days]
residual = [x-y for x,y in zip(down_time,predictedResults)]
plt.scatter(no_of_live_days,down_time)
line2,= plt.plot(no_of_live_days,predictedResults)
plt.xlabel("down_time")
plt.title("Best fit line")
plt.ylim(ymax = 1300, ymin = -100)
plt.xticks([i*150 for i in range(-1,8) ])
plt.show()
print("______________________________________________________________")
def sumsOfSquares(x):
	return sum([i**2 for i in x])

print("Sum Of Squares(Live Days): ", sumsOfSquares(no_of_live_days))
print("Sum Of Squares(Sales Values): ", sumsOfSquares(down_time))
print("______________________Confidence Interval_____________________")
#For the confidence interval I made new codes for the mean,stdev,variance
#covariance and sum of squares. I did this to make sure that the output would be
#correct

#SciPy is used to handle the confidence interval of both data lists
#SciPy contains the function norm, in this case I used stats.norm.ppf.
#ppf/pdf is the probability density function
#https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.stats.norm.html

#The two data list I chose was the down time and no of days live. From all of the data sets
# the two choses are easy to interpret since they are perfect and they contain no missing data
#that might skew the results.
def mean(x):
	return sum(x)/len(x)	
def mean2(x):
	xList = mean(x)
	return[x_i-xList for x_i in x]
def sumOfSquares(x):
	return sum([i**2 for i in x])
def var(x):
	listLength = len(x)
	dev = mean2(x)
	return sumOfSquares(dev)/(x-1)	
def standard_dev(x):
	return math.sqrt(variance(x))
#To obtain the confidence interval of both list,
#first we need the lenght of the lists and then the mean.
size1 = len(no_of_live_days)
mean3 = mean(no_of_live_days)
pop_stdev = standard_dev(no_of_live_days) 
size2 = len(down_time)
mean4 = mean(down_time)
pop_stdev1 = standard_dev(down_time) 
statistics = stats.norm.ppf(q = 0.075) 
m_o_g1 = -statistics * (pop_stdev/math.sqrt(size1))
cInterval1 = (mean3 - m_o_g1,mean3 + m_o_g1)  					   
m_o_g2 = -statistics * (pop_stdev1/math.sqrt(size2))
cInterval2 = (mean4 - m_o_g2,mean4 + m_o_g2)  
print("Confidence Interval(Live Days):",cInterval1)
print("Confidence Interval (Down Time):",cInterval2)
print("live days sample mean: ",mean3)
print("down time: ", mean4)
print("live days: ", pop_stdev)
print("down time: ", pop_stdev1)
print("_________________________________________________________")

plt.scatter(no_of_live_days,down_time)
plt.ylabel("No of days live")
plt.xlabel("Down time")
plt.title("No of days live vs. Down time")
plt.show()