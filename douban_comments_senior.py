#coding=utf-8
'''
@Conan
3.7作业
豆瓣某本书前50条短评内容及平均分
'''
import requests, re
from bs4 import BeautifulSoup as bs

url = 'https://book.douban.com/subject/4882120/comments/hot?p='
contents = []
regex = re.compile(r'\w*allstar(\d+)\w*')
stars = []
sum = 0
i = 1
while len(stars)<50: #有的人只评论了，没打星，所以星会比评论少
    print i
    req_url = url + str(i)
    res = requests.get(req_url).text
    soup = bs(res, 'html.parser')
    comment_content =  soup.find_all('p', class_ = 'comment-content')
    comment_star = soup.find_all('span', class_ = 'user-stars')
    stars.extend(comment_star)
    contents.extend(comment_content)
    i += 1

for i in range(50):
    print contents[i].get_text()
    star = regex.findall(str(stars[i]))[0]
    sum += int(star)

print sum/50
