#!/usr/bin/env python 
import sys

get_input = sys.argv[1]
ascii = []
with open (get_input, 'r') as f:
	for i in f:
		for each_type in i.split():
			if each_type[:2] == '0x':
				ascii += chr(int(each_type, base=16))
			elif each_type[:2] == '0b':
				ascii += chr(int(each_type, base=2))
			elif each_type[:1] != '0':
				ascii += chr(int(each_type, base=10))
			else:
				ascii += chr(int(each_type, base=8))
print ''.join(ascii)