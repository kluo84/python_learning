#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import time
import re
import string


sp500_symbols = []

def get_short(sym):
    short_statistic_url = "https://finance.yahoo.com/quote/"+ sym + "/key-statistics?p=" + sym
    
    short_request = requests.get(short_statistic_url).text
    short_soup = BeautifulSoup(short_request, 'lxml')
    short_value = short_soup.find_all("td", class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")
    values =[]
    for value in short_value:
        values.append(value)
    return (values[15].text)

# Get SYMBOL from S&P500 sites
def get_SP500_sym():
    sp500 = "https://www.liberatedstocktrader.com/sp-500-companies-list-alphabetically-sorted/"
    r_sp500 = requests.get (sp500).text
    sp500_soup = BeautifulSoup(r_sp500, 'lxml')
    SYM = sp500_soup.find('table', {'width':490})
    for i in SYM.findAll('td'):
        if re.search('[A-Z]+$', i.text) and len(i.text) < 7:
            sp500_symbols.append(i.text.strip())
    
get_SP500_sym()

f = open("S&P500_All.txt", "w")
        
for s in sp500_symbols:
    try:
        #s = symbol.strip() 
        yahoo = 'https://finance.yahoo.com/quote/' + s + '?p=' + s + '&tsrc=fin-srch'
        r = requests.get(yahoo).text
        soup = BeautifulSoup(r,'lxml')       
        stock_name = soup.find ("h1", class_='D(ib) Fz(18px)').text
        fair_value = soup.find("div", class_='Fw(b) Fl(end)--m Fz(s) C($primaryColor').text
        short_value = get_short(s)
        print('{:<50s}{:>20s}{:>10s}'.format(stock_name,fair_value,short_value))
        f.write('{:<50s}{:>20s}{:>10s}{}'.format(stock_name,fair_value,short_value,'\n'))
        time.sleep(5)    

    except:
        pass
        time.sleep(5)

f.close()
