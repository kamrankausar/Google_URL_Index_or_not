# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:26:37 2019

@author: genius
"""

import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.parse import urlencode

seconds = 3
#urls =

proxies = {
    'https' : 'https://localhost:8123',
    'http' : 'http://localhost:8123'
    }
    
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
headers = { 'User-Agent' : user_agent}

df = pd.read_excel('url_links.xlsx')
#df['links']
for i in range(0, len(df)):
    line = df.loc[i,'links']
    #print(line)
    if line:
        query = {'q': 'site:' + line}
        google = "https://www.google.com/search?" + urlencode(query)
        data = requests.get(google, headers=headers)
        data.encoding = 'ISO-8859-1'
        soup = BeautifulSoup(str(data.content), "html.parser")
        try:
            check = soup.find(id="rso").find("div").find("div").find("div").find("div").find("div").find("a")["href"]
            print("URL is Index ")
        except AttributeError:
            print("URL Not Index")
        time.sleep(float(seconds))
    else:
        print("Invalid Url")
"""
# Index 

#line = "https://www.citibank.com.sg/mbol/promo/html/cc_cards/instant-rewards.html"
#line = "https://www.citibank.com.sg/mbol/promo/html/cc_cards/malls.htm"
#line = "https://www.citibank.com.sg/mbol/promo/html/cc_cards/malls.html"
line = "https://www.citibank.com.sg/mbol/promo/html/cc_cards/shopping.htm"

# Not Index 
#line = "https://www.citibank.com.sg/mbol/promo/html/aj_dining_2bonus_miles_250.htm"
#line = "https://www.citibank.com.sg/mbol/promo/html/aj_dining_1cashback_500.htm"
#line = "https://www.citibank.com.sg/mbol/promo/html/aj_dining_1cashback_800.htm"
#line = "https://www.citibank.com.sg/mbol/promo/html/aj_dining_2bonus_miles_250.htm"

query = {'q': 'site:' + line}
google = "https://www.google.com/search?" + urlencode(query)
data = requests.get(google, headers=headers)
data.encoding = 'ISO-8859-1'
soup = BeautifulSoup(str(data.content), "html.parser")
print("\n")
#soup.find(id="rso")
try:
    check = soup.find(id="rso").find("div").find("div").find("div").find("div").find("div").find("a")["href"]
    print("URL is Index ")
except AttributeError:
    print("Link Not Index")

time.sleep(float(seconds))
"""
