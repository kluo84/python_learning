#!/usr/bin/env python

import sys

with open (sys.argv[1], 'r') as f:
	for line in f:
		print sum(map(lambda x: int(x, base = 16), line.split()))