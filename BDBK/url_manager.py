# -*- coding: utf-8 -*-
class UrlManager(object):

    #构造函数
    def __init__(self):
        self.new_urls.set()
        self.old_urls.set()

    #向管理器添加一个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #向管理器添加批量URL
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #判断URL管理器中是否有待爬取的URL
    def has_new_url(self):
        len(self.new_urls) != 0

    #在URL管理器中得到一个待爬取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


