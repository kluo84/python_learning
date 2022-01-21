#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import time
import re
import string


sp500_symbols = ['AAPL', 'MSFT', 'GOOG', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'NVDA', 'BRK.B', 'JPM', 'UNH', 'V', 'JNJ', 'HD', 'WMT', 'PG', 'BAC', 'MA', 'PFE', 'DIS', 'AVGO', 'XOM', 'ACN', 'CSCO', 'NFLX', 'NKE', 'LLY', 'KO', 'TMO', 'CRM', 'COST', 'ABT', 'ABBV', 'PEP', 'ORCL', 'CMCSA', 'CVX', 'PYPL', 'DHR', 'VZ', 'INTC', 'QCOM', 'WFC', 'MCD', 'MRK', 'UPS', 'T', 'AMD', 'NEE', 'MS', 'INTU', 'TXN', 'LIN', 'LOW', 'SCHW', 'UNP', 'PM', 'TMUS', 'MDT', 'HON', 'AMAT', 'BLK', 'CVS', 'BMY', 'SBUX', 'EL', 'AMT', 'GS', 'AXP', 'RTX', 'ISRG', 'PLD', 'AMGN', 'NOW', 'C', 'BA', 'IBM', 'CHTR', 'ANTM', 'CAT', 'TGT', 'SPGI', 'ZTS', 'DE', 'MU', 'GE', 'ADP', 'MMM', 'LRCX', 'SYK', 'BKNG', 'LMT', 'COP', 'MRNA', 'ADI', 'MDLZ', 'GILD', 'CCI', 'TJX', 'SHW', 'GM', 'MO', 'PNC', 'F', 'USB', 'MMC', 'CB', 'CSX', 'CME', 'EW', 'DUK', 'HCA', 'CI', 'ITW', 'EQIX', 'ICE', 'SO', 'BDX', 'MCO', 'CL', 'FISV', 'FIS', 'FDX', 'WM', 'REGN', 'ETN', 'KLAC', 'ECL', 'PSA', 'APD', 'AON', 'D', 'COF', 'ADSK', 'NXPI', 'BSX', 'NOC', 'FCX', 'HUM', 'PGR', 'ILMN', 'GD', 'VRTX', 'JCI', 'EXC', 'SNPS', 'XLNX', 'EMR', 'DG', 'FTNT', 'IDXX', 'MAR', 'EOG', 'MET', 'TEL', 'ATVI', 'SPG', 'IQV', 'INFO', 'APH', 'ALGN', 'MNST', 'CDNS', 'DXCM', 'DLR', 'ROP', 'MSCI', 'MCHP', 'NEM', 'PAYX', 'BK', 'CNC', 'KMB', 'AIG', 'CMG', 'STZ', 'A', 'CTSH', 'ORLY', 'TT', 'WBA', 'PXD', 'CARR', 'MSI', 'APTV', 'AEP', 'SLB', 'KHC', 'CTAS', 'TROW', 'ANET', 'BAX', 'HLT', 'RSG', 'SBAC', 'AZO', 'SRE', 'DOW', 'EBAY', 'DD', 'PRU', 'LHX', 'HPQ', 'GPN', 'PH', 'GIS', 'O', 'PPG', 'SYY', 'MPC', 'SIVB', 'YUM', 'ROST', 'ODFL', 'HSY', 'ROK', 'AFL', 'MTD', 'TRV', 'EA', 'MTCH', 'ADM', 'IFF', 'MCK', 'RMD', 'DHI', 'WELL', 'KEYS', 'KMI', 'XEL', 'EPAM', 'CBRE', 'OTIS', 'BIIB', 'VRSK', 'FAST', 'TDG', 'AVB', 'FRC', 'CPRT', 'DFS', 'EFX', 'AJG', 'ARE', 'STT', 'ANSS', 'CTVA', 'TWTR', 'AMP', 'EQR', 'ALL', 'NDAQ', 'PEG', 'BF.B', 'AWK', 'AME', 'KR', 'PSX', 'WST', 'NUE', 'WMB', 'DLTR', 'GLW', 'VLO', 'TSN', 'CMI', 'ZBRA', 'LYB', 'DVN', 'WY', 'PCAR', 'ES', 'FITB', 'EXR', 'SWK', 'WEC', 'BLL', 'ED', 'LVS', 'WLTW', 'OXY', 'VFC', 'LH', 'EXPE', 'VRSN', 'CDW', 'ALB', 'ABC', 'VMC', 'MLM', 'CERN', 'TER', 'ZBH', 'TSCO', 'LYV', 'OKE', 'HRL', 'ETSY', 'IT', 'SWKS', 'MAA', 'FTV', 'GWW', 'LUV', 'BKR', 'DAL', 'SYF', 'GRMN', 'DOV', 'EIX', 'MKC', 'DRE', 'STX', 'NTRS', 'ENPH', 'CHD', 'BBY', 'PAYC', 'IR', 'STE', 'PKI', 'URI', 'HES', 'HIG', 'DTE', 'ESS', 'AEE', 'MPWR', 'PPL', 'FE', 'ETR', 'ULTA', 'WAT', 'EXPD', 'BIO', 'K', 'POOL', 'GNRC', 'TRMB', 'RF', 'CLX', 'HAL', 'TYL', 'MGM', 'RJF', 'CTLT', 'JBHT', 'BR', 'XYL', 'VIAC', 'VTR', 'CFG', 'HPE', 'COO', 'FOX', 'FOXA', 'TDY', 'RCL', 'TTWO', 'KMX', 'WDC', 'NTAP', 'MTB', 'FANG', 'DGX', 'DPZ', 'NVR', 'CZR', 'GPC', 'PEAK', 'BRO', 'PFG', 'DRI', 'TECH', 'AKAM', 'SBNY', 'FLT', 'CMS', 'UDR', 'HOLX', 'CRL', 'CE', 'CINF', 'AMCR', 'IP', 'J', 'BXP', 'BBWI', 'FDS', 'DISH', 'QRVO', 'IEX', 'AVY', 'WAB', 'CNP', 'VTRS', 'LKQ', 'MAS', 'TXT', 'BEN', 'ABMD', 'ROL', 'INCY', 'CAG', 'AES', 'EMN', 'PWR', 'CTRA', 'CDAY', 'OMC', 'TFX', 'EVRG', 'NLOK', 'LNT', 'MOS', 'KIM', 'IRM', 'CF', 'MKTX', 'FFIV', 'SEDG', 'SJM', 'IPG', 'AAP', 'L', 'UAL', 'CAH', 'PTC', 'WRB', 'FBHS', 'PHM', 'WHR', 'HAS', 'CHRW', 'FMC', 'ATO', 'HWM', 'CBOE', 'NWSA', 'NWS', 'AOS', 'CPB', 'MRO', 'LUMN', 'REG', 'PKG', 'JKHY', 'LDOS', 'DISCA', 'DISCK', 'LNC', 'MHK', 'XRAY', 'HST', 'CTXS', 'RHI', 'AAL', 'DVA', 'PNR', 'WRK', 'CMA', 'ALLE', 'JNPR', 'SNA', 'TPR', 'BWA', 'NI', 'IVZ', 'RE', 'HSIC', 'FRT', 'UHS', 'NRG', 'TAP', 'APA', 'WYNN', 'ZION', 'SEE', 'GL', 'NWL', 'LW', 'UAA', 'UA', 'IPGP', 'NCLH', 'RL', 'AIZ', 'PENN', 'DXC', 'VNO', 'OGN', 'PNW', 'PBCT', 'NLSN', 'PVH', 'HII', 'GPS', 'ALK']

def get_short(sym):
    short_statistic_url = "https://finance.yahoo.com/quote/"+ sym + "/key-statistics?p=" + sym
    user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    short_request = requests.get(short_statistic_url,headers=user_agent).text
    short_soup = BeautifulSoup(short_request, 'lxml')
    short_value = short_soup.find_all("td", class_="Fw(500) Ta(end) Pstart(10px) Miw(60px)")
    values =[]
    for value in short_value:
        values.append(value)
    return (values[15].text)    

f = open("S&P500_All.txt", "w")

print('{:<50s}{:>20s}{:>20s}{:>20s}{:>20s}{:>20}'.format('Stock Name','Stock Price', 'Value', 'Short Value', 'Dividend Yield', ' Ex-Dividend Date'))

for s in sp500_symbols:
    try:
        yahoo = 'https://finance.yahoo.com/quote/' + s + '?p=' + s + '&tsrc=fin-srch&guccounter=1'
        user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        r = requests.get(yahoo,headers=user_agent).text
        soup = BeautifulSoup(r,'lxml') 
        stock_name = soup.find ("h1", class_='D(ib) Fz(18px)').text
        
        stock_price = soup.find("fin-streamer", {'data-test':'qsp-price'}).text
        
        fair_value = soup.find("div", class_='Fw(b) Fl(end)--m Fz(s) C($primaryColor').text
        
        short_value = get_short(s)
        
        dividend_yield = soup.find("td", {'data-test':'DIVIDEND_AND_YIELD-value'}).text
        ex_dividend_date = soup.find('td', {'data-test':'EX_DIVIDEND_DATE-value'}).text
        
        print('{:<50s}{:>20s}{:>20s}{:>20s}{:>20s}{:>20}'.format(stock_name,stock_price,fair_value,short_value, dividend_yield, ex_dividend_date))
        f.write('{:<50s}{:>20s}{:>20s}{:>20s}{:>20s}{:>20}{}'.format(stock_name,stock_price,fair_value,short_value,dividend_yield,ex_dividend_date,'\n'))
        time.sleep(5)    

    except:
        print(f'error in {s}')
        time.sleep(5)

f.close()
