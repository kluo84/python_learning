#!/usr/bin/env python

import sys

with open (sys.argv[1], 'r') as f:
    a = ''

    for i in f.read().split():
        a += bytearray.fromhex(i).decode()
print ''.join(a)
