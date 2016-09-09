# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import leancloud
from leancloud import Object

'''
从runningwarehouse获取Hokaoneone的数据,包括名称/价格/介绍/重量
数据获取后保存到云端-leanCloud
'''
class One:
    def __init__(self):
        leancloud.init("NIQK1VK7ULc6foDGAYCufNXP-gzGzoHsz", "t0aJoyo5QR6O85t8gyawJrMg")
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

            saveHoka = Hokaoneone()

            detail_response = requests.get(url["href"], headers=self.header)
            detail_html = detail_response.text
            detail_soup = BeautifulSoup(detail_html, 'html.parser')

            # 鞋子的名称
            name = detail_soup.body.h1.string
            saveHoka.set('name', name).save()

            # 鞋子的价格
            if detail_soup.body.div.find("span", attrs={"class": "price"}):
                price = detail_soup.body.div.find_all("span", attrs={"class": "price"})[0].string.split(" ")[1]
            else:
                price = detail_soup.body.div.find_all("span", attrs={"class": "sale"})[0].string.split(" ")[1]
            saveHoka.set('price', price).save()

            # 鞋子的详情介绍
            divs = detail_soup.body.div.find_all("div", attrs={"class": "left_column fl"})
            details = ""
            for div in divs:
                ps = div.find_all("p")
                for p in ps:
                    details += p.string
            saveHoka.set('details', details).save()

            # 鞋子重量介绍
            weigthdivs = detail_soup.body.find_all("div", attrs={"class": "right_column fr"})
            weight = weigthdivs[0].find_all("p")[1].contents[1].split(" ")[1]
            # weightKE = 28.35
            saveHoka.set('weight', weight).save()

'''
实体类用来存储到 Leancloud
'''
class Hokaoneone(Object):
    # name
    @property
    def name(self):
        return self.get('name')
    @name.setter
    def name(self, value):
        return self.set('name', value)

    # price
    @property
    def price(self):
        return self.get('price')
    @price.setter
    def price(self, value):
        return self.set('price', value)

    # details
    @property
    def details(self):
        return self.get('details')
    @details.setter
    def details(self, value):
        return self.set('details', value)

    # weight
    @property
    def weight(self):
        return self.get('weight')
    @weight.setter
    def weight(self, value):
        return self.set('weight', value)


hokaurl = 'http://www.runningwarehouse.com/catpage-HOKAM.html'
one = One()
one.getContent(hokaurl)
