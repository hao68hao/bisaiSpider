# -*- coding: utf-8 -*-
import re
import BeautifulSoup
from bs4 import BeautifulSoup

html_doc = """
<div class="product_wrapper cf">
    <div class="name w_new ">
    <a href="http://www.runningwarehouse.com/HOKA_ONE_ONE_Clifton_3_Mens_Shoes_Blue_Red_Orange/descpage-HOCL3M2.html">HOKA ONE ONE Clifton 3 Men's Shoes Blue/Red Orange</a>
    <span class="producttag newtag">New</span>
    </div>

    <div class="image_wrap">
        <a href="http://www.runningwarehouse.com/HOKA_ONE_ONE_Clifton_3_Mens_Shoes_Blue_Red_Orange/descpage-HOCL3M2.html">
            <img src="http://img.runningwarehouse.com/watermark/rs.php?path=HOCL3M2-1.jpg&amp;nw=165"/>
        </a>
    </div>
    <span class="pricing"> <span class="price">Price: $130.00</span> </span>
    <div class="text_wrap">
        <p>The HOKA ONE ONE Clifton 3 is a low heel-toe offset, performance neutral running shoe best suited for daily or uptempo training and a neutral or supinated foot motion.</p>
        <span class="shoe_links"> <a class="threesixty view360" href="http://www.runningwarehouse.com/360view.html?pcode=HOCL3M2">360° view</a>
            <a class="feedback" href="http://www.runningwarehouse.com/feedback-HOCL3M2.html">feedback</a>
        </span>
    </div>
</div>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print "\n:::获取鞋子的名称:::"
links = soup.find_all('a')[0]
for link in links:
    # print link.name, link['href'], link.get_text()
    print link


#打印鞋子简介的三种方式
print "\n:::获取鞋子简介文字,使用三种不同的方式并且打印出来类型::::::"
p_nodeContents = soup.find("p").contents[0].split(" ")[13]
p_nodeContentss = soup.find("p").contents[0]
print '\np_nodeContents:',p_nodeContents
print '\np_nodeContentss:',p_nodeContentss
print '\np_nodeContentss:',type(p_nodeContentss)



p_nodeString = soup.find("p").string[4]
print '\np_nodeString:',p_nodeString
print '\np_nodeString:',type(p_nodeString)

p_nodeGetText = soup.find('p')
print "\np_nodeGetText:",p_nodeGetText.get_text()
print "\np_nodeGetText:",type(p_nodeGetText.get_text())

#打印鞋子详情页的链接
print ":::打印鞋子详情页的链接:::"
detail_Url = soup.find('a')
print detail_Url['href']

