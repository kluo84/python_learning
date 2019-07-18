#!/usr/bin/env python
import requests
import sys

r = requests.get(sys.argv[1])
print r.content


