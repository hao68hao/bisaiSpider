#-*- coding:utf-8 -*-

'''
import time
print 'how'
time.sleep(2)
print 'are'
time.sleep(2)
print 'you'
time.sleep(2)
print 'today?'
time.sleep(2)

from time import sleep
print '过两秒后会出现另一个字'
sleep(2)
print '就是这个'



import random
i = random.randint(1,101)
print i

l = random.random()
print l

k = random.random() * 100
print k
'''

print 'Number \tSquare \tCube'
for i in range(1,11):
    print i, '\t', i**2, '\t', i**3

name = 'today is bad!'
print 'today is good and', name, 'or right'

name1 = 'today is bad!'
print 'today is good and %s or right' % name1

age = 12
print '我今年%i岁' % age

average = 76.5
print '平均是有%f的比例' % average

'''
%s 插入字符串
%i 插入整数
%f 插入浮点数
'''