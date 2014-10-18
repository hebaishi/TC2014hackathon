# -*- coding: utf-8 -*-
import requests
import bs4
import re

root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'

url = 'http://www.amazon.co.uk/gp/aw/s/ref=is_box_?k=trousers'


if __name__ == '__main__':
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    for link in soup.find_all('a'):
        if (re.search('qid=',str(link.get('href')))):        
            line = ""
            line = "DESC " + str(link.string)
            line += " LINK " + str(link.get('href'))        
            prodlink = "http://www.amazon.co.uk/"+str(link.get('href'))
            response2 = requests.get(prodlink)
            soup2 = bs4.BeautifulSoup(response2.text)        
            for imgs in soup2.find_all('img'):
                if (str(imgs.get('id')) == "detailImg"):            
                    line += "IMG " + imgs.get('src')
            m=re.findall('£(\d+)\.(\d+)',str(response2.text),re.I)
            price = str(m.group(1)) + "." + str(m.group(2))        
            line += " PRICE "+ price
            print line