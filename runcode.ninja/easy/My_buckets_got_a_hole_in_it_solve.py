#!/usr/bin/env python 
import sys

get_input = ' '.join(sys.argv[1:])

groups = [0 for i in range(1000)]
maximum = 0

with open (get_input, 'r') as f:
	for line in f:
		num = int(line)
		groups[num // 10] += 1
		maximum = max(maximum, num //10)
		
# create the output string
output = ''
for i in range(maximum + 1):
	output += str(groups[i])
print output