#!/usr/bin/env python

import sys, string

alphabet = string.ascii_letters

with open (sys.argv[1], 'r') as f:
    for line in f:
        if len(line.split())>1:
            try:
                l, r = map(int, line.split())
                print l + r
            except Exception:
                try:
                    l,r = map (float, line.split())
                    print l + r
                except Exception:
                    pass
