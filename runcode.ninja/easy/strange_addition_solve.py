#!/usr/bin/env python
import sys

with open (sys.argv[1], 'r') as f:
    for line in f:
        for i in line.split('\n'):
            if len(i) > 1:
                a =  sum(map(lambda x: int(x), i.split()))
                print a + len(i.split())
