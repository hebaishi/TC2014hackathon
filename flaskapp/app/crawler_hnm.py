# -*- coding: utf-8 -*-
import requests
import bs4
import re





def bankcrawl(params):
    prodlist = list()    
    k=re.sub(r'\s+',r'+',params['keywords']) 
    if (params['gender'] == 'Male'):
          url = 'http://www.bankfashion.co.uk/products/search?q=men+' + k
    else:
          url = 'http://www.bankfashion.co.uk/products/search?q=women+' + k   
    print url
    h= float(params['height'])/100     
    bmi = float(params['weight'])/(h*h)
    print "bmi is " + str(bmi)    
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text.encode('utf-8'))
    #print response.text    
    prodlink = list()    
    for link in soup.find_all('a'):
                    if (str(link.get('class')) == 'itemInfo'): 
                        print str(link.get('class')) 
                        prodlink.append(str(link.get('href')))
                        print prodlink
    imgl = list()
    price = list()
    des = list()
    for plink in range(len(prodlink)):
        d = dict()
        d['link'] = prodlink[plink]  
        responsep = requests.get(prodlink[plink])
        soupp = bs4.BeautifulSoup(responsep.text.encode('utf-8'))
        m = re.search('[\w./:-]+image1xl[\w.]+', str(soupp))
        d['img'] = m.group(0)
        p = re.search('ProductPriceText":"£([\d.]+)', str(soupp))
        d['cost'] = p.group(1)
        d1 = re.search('ProductName":"([\.\-\w\s]+)', str(soupp)).group(1)
        d['desc'] = d1
        d['site'] = 'http://content.asos-media.com/~/media/240613124858/Images/uk/Archive/june/asos-logo.png'
        prodlist.append(d)
    return prodlist
        

if __name__ == '__main__':
    par = dict()
    par['height'] = 12
    par['weight'] = 12
    par['gender'] = 'Male'
    par['keywords'] = "shirt red"
    pl = bankcrawl(par)                   