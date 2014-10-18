# -*- coding: utf-8 -*-
import requests
import bs4
import re


url = 'http://www.asos.com/search/shirt?q=shirt'

if __name__ == '__main__':
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    prodlink = list()    
    for link in soup.find_all('a'):
         if (re.search(r'iid',str(link.get('href')))):        
            prodlink.append(str(link.get('href'))) 
            
            
