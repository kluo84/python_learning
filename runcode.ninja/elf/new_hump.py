#!/usr/bin/env python3

import sys, os, subprocess, re, glob

flag = ""
def sorted_smart(string):
	rlen(string)-7
#Getting the file paths
for infile in sorted(glob.glob(os.path.join(sys.argv[1], '*.bin')),key = lambda x: x[len(x)-7]):
	a = subprocess.run(infile, stdout=subprocess.PIPE)
	flag += a.stdout.decode('utf-8')
blah = flag.split()
flag_merge = ('_'.join(blah))
print ("CWN{" + flag_merge + "}")