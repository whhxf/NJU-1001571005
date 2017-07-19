#coding=utf-8
'''
@Conan
豆瓣短评爬取，课程3.2
'''
import requests
from bs4 import BeautifulSoup as bs
import re
import math

url = 'https://book.douban.com/subject/26883531/comments/'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
comment_content = soup.find_all('p', class_ = 'comment-content')
comment_star = soup.find_all('span', class_ = 'user-stars')
for i in comment_content:
   print i.get_text()
regex = re.compile(r'\w*allstar(\d+)\w*')
comment_stars = []
for i in comment_star:
    star =regex.findall(str(i))[0]
    comment_stars.append(star)
print comment_stars 
