# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.jianshu.com/users/65ed1c462691/top_articles'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(url, headers=header)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

author_info = soup.find_all('ul', class_='clearfix')

info = author_info[0]
print '\n 作者信息==============:\n',info
numbers = info.find_all('b')
print '\n 有用的数据============\n',numbers
number_list = [int(item.string) for item in numbers]
name = soup.find('title')
name.string
# print '\n 有用的数据数组============\n',number_list
# print '\n 文章的名称============\n',name

author_name = name.string[:-5]
# print '\n 作者的名称============\n',author_name

def author(name, number_list):
    author_dict = {}
    author_dict['name'] = name
    author_dict['following'] = number_list[0]
    author_dict['fans'] = number_list[1]
    author_dict['articles'] = number_list[2]
    author_dict['words'] = number_list[3]
    author_dict['likes'] = number_list[4]
    return author_dict

def print_author(author_dict):
    print(author_dict['name'], '有', author_dict['fans'], '个粉丝，写了', author_dict['articles'],
          '篇文章，码了', author_dict['words'], '个字，\n收割了', author_dict['likes'],
          '颗喜欢， 他悄悄关注了', author_dict['following'], '人~~~')

cesc = author(author_name, number_list)
print '\n print_author============\n'
print_author(cesc)