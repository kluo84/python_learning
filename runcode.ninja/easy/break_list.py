#!/usr/bin/env python 
import sys
import string

numbers = ['0','1','2','3','4','5','6','7','8','9']
get_input = sys.argv[1]
num_list = []
sub_list = []

with open (get_input, 'r') as f:
	for line in f:
		for item in line.split():
			if item in numbers and len(item) < 3:
				num_list += (item)
			elif len(item) > 3:
				for sub_item in item.split():
					if (sub_item) in numbers:
						sub_list += sub_item
					num_list.append(sub_list)
print num_list
