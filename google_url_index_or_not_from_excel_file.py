#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:18:43 2019

@author: kamran
"""

import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from urllib.parse import urlencode


seconds = int(input('Enter the Sleep time:- '))
proxies = {
    'https' : 'https://localhost:8123',
    'http' : 'http://localhost:8123'
    }

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
headers = { 'User-Agent' : user_agent}

# Change the File Name
file_name = input("Please Enter the file name:- ")
col_name = input("Please Enter the Column Name:- ")
#df = pd.read_excel('url_index_or_not.xlsx')
df = pd.read_excel(file_name)
df_result = pd.DataFrame()
for i in range(0, len(df)):
    line = df.loc[i,col_name]
    #print(line)
    if line:
        query = {'q': 'site:' + line}
        google = "https://www.google.com/search?" + urlencode(query)
        data = requests.get(google, headers=headers)
        data.encoding = 'ISO-8859-1'
        soup = BeautifulSoup(str(data.content), "html.parser")
        try:
            check = soup.find(id="rso").find("div").find("div").find("div").find("div").find("div").find("a")["href"]
            print(line, ':- Index')
            df_result.loc[i, 'links'] = line
            df_result.loc[i, 'result'] = 'index'
        except AttributeError:
            print(line,':- Not Index')
            df_result.loc[i, 'links'] = line
            df_result.loc[i, 'result'] = 'not index'
    
    else:
        print("Invalid Url")
    time.sleep(float(seconds))
    
df_result.to_excel('url_index_result.xlsx', index = False)
