# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

class HokaRWH():
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self):
        url = 'http://www.runningwarehouse.com/catpage-HOKAM.html'
        req = requests.get(url, headers=self.headers)
        return req

    def getItem(self):
        req = self.getPage()
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            tableContent = soup.body.table.find_all('div', 'product_wrapper cf')
            for link in tableContent.p:
                print link


hoka = HokaRWH()
hoka.getItem()




        # req = self.getPage(pageIndex)
        # if req.status_code == 200:
        #     print '第', pageIndex, '页下载完成'
        #     soup = BeautifulSoup(req.content, 'html.parser')
        #     for link in soup.find_all('div', 'post'):
        #         title = link.a['title']
        #         ids = link.a['data-id']
        #         imgUrl = link.a.contents[1]['src']
        #         jieshao = link.find_all('p')[1].string
        #         detailUrl = link.a['href']
        #         detail = self.getDetailContent(link.a['href'])
        #         print title, ids, imgUrl, jieshao, detailUrl, detail
