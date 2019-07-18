#!/usr/bin/env python

import sys

with open (sys.argv[1], 'r') as f:
	try:
		for line in f:
			l, r = map(int, line.split())
			print l + r
	except Exception:
		try:
			l, r = map(float, line.split())
			print l+r
		except Exception:
			pass

