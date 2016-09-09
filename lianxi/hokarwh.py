# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

class One:
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.header = {'User-Agent': self.user_agent}

    def getContent(self,hokaurl):

        response = requests.get(hokaurl, headers=self.header)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        urls = soup.body.find_all("a", href=re.compile(r'HOKA_ONE_ONE'))

        for url in urls:
            if url["href"].find("descpage") == -1:
                continue

            detail_response = requests.get(url["href"], headers=self.header)
            detail_html = detail_response.text
            detail_soup = BeautifulSoup(detail_html, 'html.parser')

            # 鞋子的名称
            name = detail_soup.body.h1.string

            # 鞋子的价格
            if detail_soup.body.div.find("span", attrs={"class": "price"}):
                price = detail_soup.body.div.find_all("span", attrs={"class": "price"})[0].string.split(" ")[1]
            else:
                price = detail_soup.body.div.find_all("span", attrs={"class": "sale"})[0].string.split(" ")[1]

            # 鞋子的详情介绍
            divs = detail_soup.body.div.find_all("div", attrs={"class": "left_column fl"})
            details = ""
            for div in divs:
                ps = div.find_all("p")
                for p in ps:
                    details += p.string

            # 鞋子的图片
            # imgUrlDivs = detail_soup.body.div.find_all("img", attrs={"height":"262"})
            # imgUrl = imgUrlDivs



            # 鞋子重量介绍
            weigthdivs = detail_soup.body.find_all("div", attrs={"class": "right_column fr"})
            weight = weigthdivs[0].find_all("p")[1].contents[1].split(" ")[1]
            # print "\n鞋子名称:",name
            # print "\n鞋子价格:",price
            # print "\n鞋子重量:",float(weight) * 28.35
            # print "\n鞋子介绍:",details
            # print "=================================="

hokaurl = 'http://www.runningwarehouse.com/catpage-HOKAM.html'
one = One()
one.getContent(hokaurl)
