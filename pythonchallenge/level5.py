import requests,re
import string
import pickle

#######################
###Level5
#######################

url = 'http://www.pythonchallenge.com/pc/def/'
#url_5  = url + 'peak.html'
url_5  = url + 'banner.p'
#print "Level 5 url is " + url_5
r_5 = requests.get(url_5)
context_5 = r_5.text[0]

peak = pickle.load(context_5)
for i in peak:
	print i
