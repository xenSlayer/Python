"""
This python code is written by Kiran Paudel for personal use. The re use and re edit of the code is allowed and well appreciated.
This python script scraps top 'crime' movies of year 2019  from the website 'www.simkl.com' and provides links to those movies hosted on website 'www.hdeuropix.com'
The code may not be use able after some time because the link to 'hdeuropix.com' keeps changing overtime due to website policy.
Some of the movies that has character like : - . in their title links does not open up
Some movies link may not work if 'hdeuropix' has not yet uploaded the movie to their website
"""
import requests
from bs4 import BeautifulSoup

url = requests.get("https://simkl.com/movies/crime/this-year/").text
page = BeautifulSoup(url,'lxml')

for x in page.find_all('div',class_='SimklTVPosterAltText'):
    data = x.text
    link_ = data.lower()
    link_ = link_.split(' ')
    length = len(link_)
    link_[0:length] = ['-'.join(link_[0:length])]
    link_ = str("https://europixhd.io/mov/"+link_[0]+"-2019-online-free-hd-with-subtitles-europix")
    i = "*"
    print(i,"Movie Name-> ",str(data))
    print("link-> ",link_)


