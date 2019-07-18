#!/usr/bin/env python

import sys

def rev(word):
    return word[::-1]

def check_Pa(word):
    r = rev(word)
    # Checking if both string are equal or not 
    if (word == r): 
        return True
    return False

with open (sys.argv[1], 'r') as f:
    for line in f:
        check = check_Pa(line)
        if check == 1:
            print 'True'
        else:
            print 'False'
