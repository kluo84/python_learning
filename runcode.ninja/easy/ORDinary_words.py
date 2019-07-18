#!/usr/bin/env python

import sys

a = []
with open (sys.argv[1], 'r') as f:
    for line in f:
        for i in line.split():
            a.append (chr(int(i)))
print "".join(a)
