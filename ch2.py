from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# print all tags
html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read())
names = bsObj.findAll('span', {'class': 'green'})
for name in names:
    print(name.get_text())

# print all rows
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read())
for child in bsObj.find('table', {'id': 'giftList'}).children:
    print(child)

# print all rows except first
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read())
for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

# print parent's value
html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read())
print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())


html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)

# not good, includes logo.jpg
images = bsObj.findAll('img')
for image in images:
    print(image['src'])

# print only the relative image paths that start with ../img/gifts/img
images = bsObj.findAll('img', {'src': re.compile("\.\./img\/gifts/img.*\.jpg")})
for image in images:
    print(image['src'])
