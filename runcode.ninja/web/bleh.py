#!/usr//bin/env python3

import requests
import sys
from bs4 import BeautifulSoup as bs


r = requests.get(sys.argv[1])
post = r.content

soup = bs(post, 'html.parser')
print (soup)
