#!/usr/bin/env python
import sys

with open (sys.argv[1], 'r') as f:
	lines = f.readlines()
for line in lines:
	index, nums = line.split()
	#print max(sorted(map(int, nums.split(","))))
	biggest_num = nums[int(index)]
	for num in nums.split(","):
		if num > biggest_num:
			biggest_num = num
		if max(nums.split(",")) == biggest_num:
			print "nothing"
	print biggest_num
