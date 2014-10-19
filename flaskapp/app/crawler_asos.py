# -*- coding: utf-8 -*-
import requests
import bs4
import re





def asoscrawl(params):
    prodlist = list()    
    k=re.sub(r'\s+',r'+',params['keywords']) 
    if (params['gender'] == 'Male'):
          url = 'http://www.asos.com/search/?q=men&q=' + k
    else:
          url = 'http://www.asos.com/search/?q=women&q=' + k   
    print url
    h= float(params['height'])/100     
    bmi = float(params['weight'])/(h*h)
    print "bmi is " + str(bmi)    
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text.encode('utf-8'))
    prodlink = list()    
    for link in soup.find_all('a'):
         if (re.search(r'iid',str(link.get('href')))):        
            prodlink.append(str(link.get('href'))) 
    imgl = list()
    price = list()
    des = list()
    for plink in range(len(prodlink))[0::3]:
        d = dict()
        d['link'] = prodlink[plink]  
        responsep = requests.get(prodlink[plink])
        soupp = bs4.BeautifulSoup(responsep.text.encode('utf-8'))
        m = re.search('[\w./:-]+image1xl[\w.]+', str(soupp))
        d['img'] = m.group(0)
        p = re.search('ProductPriceText":"£([\d.]+)', str(soupp))
        if (p is None):
            continue
        else:
            d['cost'] = p.group(1)
        d1 = re.search('ProductName":"([\'\.\-\w\s]+)', str(soupp)).group(1)
        d['desc'] = d1
        d['desc'].encode('ascii', 'ignore')    
        d['site'] = 'http://content.asos-media.com/~/media/240613124858/Images/uk/Archive/june/asos-logo.png'
        prodlist.append(d)
    return prodlist
        

if __name__ == '__main__':
    par = dict()
    par['height'] = 12
    par['weight'] = 12
    par['gender'] = 'Male'
    par['keywords'] = "shirt red"
    pl = asoscrawl(par)                   