#!/usr/bin/env python
import sys

a =[]
with open (sys.argv[1], 'r') as f:
    for line in f:
        for line1 in line.split("."):
            try:
                a.append(line1.split()[0])
            except Exception:
                pass
print " ".join(a)
