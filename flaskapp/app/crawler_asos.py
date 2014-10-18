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
    imgl = list()
    price = list()
    des = list()
    for plink in range(10):
        responsep = requests.get(prodlink[plink])
        soupp = bs4.BeautifulSoup(responsep.text)
        m = re.search('[\w./:-]+image1xl[\w.]+', str(soupp))
        imgl.append(m.group(0))
        p = re.search('ProductPriceText":"([£\d.]+)', str(soupp))
        price.append(p.group(1))
        d = re.search('ProductName":"([\-\w\s]+)', str(soupp)).group(1)
        des.append(d)
                