# -*- coding: utf-8 -*-
import requests
import bs4
import re


url = 'http://mobile.ebay.co.uk/Pages/SearchResults.aspx?sflag=1&emvcc=0&nbcol=0|null'

if __name__ == '__main__':
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    for link in soup.find_all('a'):
         #if (re.search(r'aid',str(link.get('href')))):        
            print(link.get('href'))