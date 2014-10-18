import requests
import bs4
import re

root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'

url = 'http://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Dclothing&field-keywords=skirt'

def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)

if __name__ == '__main__':
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    for link in soup.find_all('a'):
        if (re.search(r'keyword',str(link.get('href')))):        
            print(link.get('href'))