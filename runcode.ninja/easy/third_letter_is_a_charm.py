#!/usr/bin/env python

import sys

with open (sys.argv[1], 'r') as f:
    for line in f:
        print " ".join(map(lambda i: (i[1:3]+i[0]+i[3:]) if len(i) > 2 else i, line.split()))
