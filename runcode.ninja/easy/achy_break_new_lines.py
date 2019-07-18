#!/usr/bin/env python

import sys

solve = []
with open (sys.argv[1], 'r') as f:
	try:
		for line in f:
			if line.split("\n")[0] != "":
				solve.append(line.split("\n")[0])
 	except Exception:
 		pass
print "\n".join(solve)