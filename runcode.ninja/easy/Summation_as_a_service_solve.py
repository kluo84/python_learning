#!/usr/bin/env python

import sys

with open (sys.argv[1], 'r') as f:
    for line in f:
        l ,r = sorted(map(int, line.split()))
        a = range(l, r+1)
        print sum(a) 
