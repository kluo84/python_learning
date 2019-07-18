#!/usr/bin/env python3

import sys
with open (sys.argv[1], 'r') as f:
    for line in f:
        l, r = sorted(map(int, line.split()))
        check_num = 1
        a = []
        while (True):
            if (check_num % 7 == 0 and check_num % 5 != 0 and check_num >= l):
                a.append (check_num) 
            check_num += 1
            if (check_num == (r+1)):
                break
        # This is special on python 3 only, print the list using * and sep operator
        print (*a, sep = ",")
