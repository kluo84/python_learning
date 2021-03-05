#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import time
import re
import string


nasdaq_symbols_not_sort = []
nasdaq_symbols = sorted(set(nasdaq_symbols_not_sort))


def get_short(sym):
    short_statistic_url = "https://finance.yahoo.com/quote/"+ sym + "/key-statistics?p=" + sym
    
    short_request = requests.get(short_statistic_url).text
    short_soup = BeautifulSoup(short_request, 'lxml')
    short_value = short_soup.find_all("td", class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")
    values =[]
    for value in short_value:
        values.append(value)
    return (values[15].text)

# Get SYMBOL from NASDQ sites
for i in string.ascii_uppercase:
    nasdaq = "https://www.advfn.com/nasdaq/nasdaq.asp?companies=" + i
    r_nasdaq = requests.get (nasdaq).text
    nasqd_soup = BeautifulSoup(r_nasdaq, 'lxml')
    SYM = nasqd_soup.find_all('a', href=True)

    for S in SYM:
        try:
            if len(S.string) < 6 and len(S.string) > 1 and S.string != None:
                nasdaq_symbols.append(S.string)
        except:
            pass

f = open("NASDAQ.txt", "w")
        
for s in nasdaq_symbols:
    try:
        #s = symbol.strip() 
        yahoo = 'https://finance.yahoo.com/quote/' + s + '?p=' + s + '&tsrc=fin-srch'
        r = requests.get(yahoo).text
        soup = BeautifulSoup(r,'lxml')       
        stock_name = soup.find ("h1", class_='D(ib) Fz(18px)').text
        fair_value = soup.find("div", class_='Fw(b) Fl(end)--m Fz(s) C($primaryColor').text
        short_value = get_short(s)
            
        if (fair_value != 'Overvalued'):
            print(stock_name + " --- " + s + " --- " + fair_value + " --- " + short_value )
            f.write(stock_name + " --- " + s + " --- " + fair_value + " --- " + short_value + "\n")
            time.sleep(5)
    except:
        pass
        time.sleep(5)

f.close()
