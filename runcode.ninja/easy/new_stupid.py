#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    for l in f:
        try:
            left, right = list(map(int, l.split()))
            print(left + right)
        except Exception:
            try:
                left, right = list(map(float, l.split()))
                print(round(left + right, 6))
            except Exception:
                pass
        except Exception:
            pass
