#!/usr/bin/env python3

import requests
import sys
import re
from bs4 import BeautifulSoup as bs


r = requests.get(sys.argv[1]+'/product/7')
response = r.content
soup = bs(response, 'html.parser')

flag = soup.find('h1',{'class':'display-4'}).text

print (flag)
