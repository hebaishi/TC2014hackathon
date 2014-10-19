# -*- coding: utf-8 -*-
import requests
import bs4
import re

# list is height, weight, gender, keywords


def amazoncrawl(params):
    prodlist = list()    
    h= float(params['height'])/100     
    bmi = float(params['weight'])/(h*h)
    print "bmi is " + str(bmi)     
    for i in range(1,5):
        k=re.sub(r'\s+',r'\+',params['keywords'])        
        if (params['gender'] == "Male"):
            g = "men"
        else:
            g = "women"        
        url = 'http://www.amazon.co.uk/gp/aw/s/ref=is_box_?k=' + str(k) + "+" + g +'&page=' + str(i)
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        for link in soup.find_all('a'):
            d = dict()
            if (re.search('qid=',str(link.get('href')))):        
                d['desc'] = link.string.encode('ascii', 'ignore') 
                d['link'] = "http://www.amazon.co.uk" + str(link.get('href'))            
                prodlink = "http://www.amazon.co.uk/"+str(link.get('href'))
                response2 = requests.get(prodlink)
                soup2 = bs4.BeautifulSoup(response2.text)        
                for imgs in soup2.find_all('img'):
                    if (str(imgs.get('id')) == "detailImg"):            
                        d['img'] = imgs.get('src')
                        break
                m=re.findall('£(\d+)\.(\d+)',response2.text.encode('utf-8'),re.I)
                price=""            
                if (m):            
                    if (len(m) == 1):
                        price = str(m[0][0]) + "." + str(m[0][1])
                    elif (len(m) == 2):
                        price = str(m[0][0]) + "." + str(m[0][1]) + " - " + str(m[1][0]) + "." + str(m[1][1])
                d['cost'] = price
                d['site'] = "http://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Amazon.com-Logo.svg/200px-Amazon.com-Logo.svg.png"            
                prodlist.append(d)
    return prodlist
            
if __name__ == '__main__':
    par = dict()
    par['height'] = 12
    par['weight'] = 12
    par['gender'] = 'Male'
    par['keywords'] = "trousers"
    pl = amazoncrawl(par)            
    
    
#    http://www.amazon.co.uk/gp/aw/s/ref=is_s_?ie=UTF8&k=trousers+xl&url=i%3Daps&page=4
#    http://www.amazon.co.uk/gp/aw/s/ref=is_pg_2_1?rh=i%3Aaps%2Ck%3Atrousers+xl&page=2&keywords=trousers+xl&ie=UTF8&qid=1413659862
#    http://www.amazon.co.uk/gp/aw/s/ref=is_pg_3_2?rh=i%3Aaps%2Ck%3Atrousers+xl&page=3&keywords=trousers+xl&ie=UTF8&qid=1413659887
