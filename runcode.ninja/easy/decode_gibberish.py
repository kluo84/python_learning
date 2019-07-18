#!/usr/bin/env python
#encoding = utf8

import sys, base64, io

def decode_b64(a):
    try:
        return base64.b64decode(a+"===")
    except Exception:
        pass

with open ('/usr/share/dict/american-english', 'r') as f:
    ae_lines = f.readlines()
        
with open (sys.argv[1], 'r') as f:
    lines = f.readlines()
for line in lines:
    while True:
        line = decode_b64(line)
        if any(line in s for s in ae_lines):
            print line
            break