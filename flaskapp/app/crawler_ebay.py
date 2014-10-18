import requests
import bs4
import re

root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'

url = 'http://www.asos.com/search/shirt?q=shirt'

def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)

if __name__ == '__main__':
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    prodlink = list()    
    for link in soup.find_all('a'):
         if (re.search(r'iid',str(link.get('href')))):        
            prodlink.append(str(link.get('href'))) 
            
            