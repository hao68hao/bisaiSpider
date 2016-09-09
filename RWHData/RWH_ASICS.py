# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

asicsurl = 'http://www.runningwarehouse.com/catpage-MRSASICS.html'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(asicsurl, headers=header)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
urls = soup.body.find_all("a",href=re.compile(r'ASICS'))

for url in urls:
    if url["href"].find("descpage") == -1:
        continue

    detail_response = requests.get(url["href"], headers=header)
    detail_html = detail_response.text
    detail_soup = BeautifulSoup(detail_html, 'html.parser')

    # 鞋子名称
    name = detail_soup.body.h1.string

    # 鞋子价格
    if detail_soup.body.div.find_all("span", attrs={"class": "price"}):
        price = detail_soup.body.div.find_all("span", attrs={"class": "price"})[0].string.split(" ")[1]
    else:
        price = detail_soup.body.div.find_all("span", attrs={"class": "sale"})[0].string.split(" ")[1]

    # 鞋子的详情介绍
    divs = detail_soup.body.div.find_all("div", attrs={"class":"left_column fl"})
    divss = divs.find_all("p")
    print divss
    # else divs.find_all():




    # 鞋子重量
    # weigthdivs = detail_soup.body.find_all("div", attrs={"class": "right_column fr"})
    # weight = weigthdivs[0].find_all("p")[1].contents[1].split(" ")[0]
    #
    # print '鞋子名称:',name
    # print '鞋子价格:',price
    # print '鞋子介绍:',details
    # print '鞋子重量:',weight
    # print '======================================='