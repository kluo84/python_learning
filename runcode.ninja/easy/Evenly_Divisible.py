#!/usr/bin/env python
import sys
'''
with open (sys.argv[1], 'r') as f:
	for line in f:
		# this is very important function to separate the numbers
		l, r = sorted(map(float, line.split()))
		temp_num = 1
		while temp_num <= r:
			if int(temp_num) == temp_num and (int(temp_num)/l).is_integer():
				print (int(temp_num))
			temp_num += 1
		print()
'''
with open (sys.argv[1], 'r') as f:
	for line in f:
		# this is very important function to separate the numbers
		l, r = sorted(map(int, line.split()))
		temp_num = 1
		while temp_num <= r:
			if temp_num == temp_num and int(temp_num)%l == 0:
				print temp_num
			temp_num += 1
		print " "
