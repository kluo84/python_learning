import requests,re
import string
import subprocess
import sys

#install prerequi
def install(package):
	subprocess.call([sys.executable, "-m", "pip","install",package])

install("urllib2")

url = "http://www.pythonchallenge.com/pc/def/"
#######################
###Level0
#######################
#first based on the picture and calculate for the number
calc = 2**38
url_0 = url + str(calc) + ".html"


#Get the map.html after follow the calc with redirection in python requests
r_0 = requests.get(url_0)
print "Level 0 url is " + r_0.url
context_0 = r_0.text
map_regex = re.findall('URL=(.*?)">',context_0)
#######################
###Level1
#######################
#Get the first match in re.findall
url_1 = url + str(map_regex[0])
print "Level 1 url is " + url_1

r_1 = requests.get(url_1)
context_1 = r_1.text
#Parsing the encrypted message in the calc_url
encrypt_msg = re.findall(r'<font color="#f000f0">\n(.*?)\n</tr></td>', context_1)
alphabet = (string.ascii_lowercase)
#get strings shift to 2 character from alphabet
#This is based on the picture on map.html
shift_2_al = ""
for i in (alphabet):
	if i == 'y':
		shift_2_al += 'a'
	elif i == 'z':
		shift_2_al += 'b'
	else:
		shift_2_al += chr(ord(i)+2)

#Create the alphabet and shift_2_al string to use maketrans() 
rot2 = string.maketrans(str(alphabet), str(shift_2_al))

print "Clue in the website that lead to maketrans() below:\n" 
print string.translate(str(encrypt_msg[0]),rot2)

#translate "map" based on rot2
url_rot2 = "map".translate(rot2)
url_2 = url + url_rot2 + ".html"
#######################
###Level2
#######################

print "Level 2 url is " + url_2
r_2 = requests.get(url_2)

context_2 = r_2.text

#Find the rare line in source with regex...===>> re.DOTALL is important
rare_char = re.findall('<!--(.*?)-->',context_2,re.DOTALL)

#rare characters are only appear once...we user count to count all the characters in the string

level2 = ''.join(re.findall('[A-Za-z]',rare_char[1]))
print "The strings for level2 answer is " + level2

#######################
###Level3
#######################
url_3 = url + level2 + ".html"
print "Level 3 url is " + url_3

r_3 = requests.get(url_3)
context_3 = re.findall('<!--(.*?)-->', r_3.text, re.DOTALL)
#One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on 
#each of its sides

level3 = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", context_3[0])
print "Level 3 answer is " + ''.join(level3)
#######################
###Level4
#######################
# URL for the level 4 is .php
url_4 = url + ''.join(level3) + ".php"
print "Level 4 url is " + url_4
r_4 = requests.get(url_4)
context_4 = r_4.text

nothing_num = (re.findall('nothing=(.*?)">', context_4))[0] # nothing_num = 12345
# Create a while loop that loop through the nothing_num 
while(True):
	try:
		level4_loop = requests.get(url_4+"?nothing="+nothing_num)
		nothing_num = (re.findall('next nothing is (\d+)', level4_loop.text))[0]
		if (re.findall('next nothing is (\d+)', level4_loop.text))[0] == '16044':
			nothing_num = str(16044/2)
		print "Checking the nothing number " + nothing_num
	except:
		l4_ans = requests.get(url_4+"?nothing="+nothing_num)
		print "Level 4 answer is " + l4_ans.text
		break
		