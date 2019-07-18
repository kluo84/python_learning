#!/usr/bin/env python 
import sys

get_input = ' '.join(sys.argv[1:])

with open(get_input, 'r') as f:
	print f.read()