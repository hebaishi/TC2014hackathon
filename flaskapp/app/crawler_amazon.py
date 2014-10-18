# -*- coding: utf-8 -*-
import requests
import bs4
import re


url = 'http://www.amazon.co.uk/gp/aw/s/ref=is_box_?k=trousers'

def amazoncrawl(params)
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
            price=""            
            if (m):            
                if (len(m)> 0):
                    price = str(m[len(m)-1][0]) + "." + str(m[len(m)-1][1])   
            line += " PRICE "+ price
            print line
            
#if __name__ == '__main__':
            