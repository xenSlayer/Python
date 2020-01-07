''''
This code is written by Kiran Paudel.
This code scrape the image link from the website https://www.pexels.com and downloads them.
The script is made completely for fun and personal use
The reuse and editing of code is appreciate
and ya sorry for my bad english :)
'''
import requests
import csv
import random
import string
from bs4 import BeautifulSoup


def randomString(stringLength=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

source = requests.get('https://www.pexels.com').text
soup = BeautifulSoup(source,'lxml')

for links in soup.find_all('a',class_='js-photo-link photo-item__link'):
    img = links.img['data-big-src']
    img = img.split('?')[0]
    download_img = requests.get(img)
    with open(randomString(20)+".jpeg",'wb') as f:
        f.write(download_img.content)
    print(img)

