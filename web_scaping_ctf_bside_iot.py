#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup as bs
import json


URL = 'http://ctf.clubbingbabyseals.org/login'
EMAIL = 'user@gmail.com'
PASSWORD = '$$$'
CHAL_URL = 'http://ctf.clubbingbabyseals.org/api/v1/challenges'
dict_equip = {}
with requests.Session() as s:
    r = s.get(URL)
    soup = bs(r.content, 'lxml')
    inpt = soup.find(attrs={'name':'nonce'})
    nonce = inpt['value']
    login_data = dict(name=EMAIL, password=PASSWORD, nonce=nonce)
    
    resp = s.post(URL, data=login_data, headers=dict(Referer=URL))

    chal = s.get(CHAL_URL)
    chal_soup = bs(chal.content, 'lxml')
    
    dict_equip = json.loads(str(chal_soup.get_text()))
    for item in dict_equip['data']:
        print(item['category'] + " " + item['name'])

