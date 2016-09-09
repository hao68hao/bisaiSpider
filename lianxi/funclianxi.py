#-*- coding:utf-8 -*-
import jieba
'''
def printMax(a,b):
    if a > b:
        print a, 'is maxmum'
    else:
        print b, 'is maxmum'


def func(x):
    print 'x is', x
    x = 4
    print 'x changed local x to', x


def func1():
    global x
    print 'x is', x
    x = 2
    print 'changed local x to', x

#函数func1
x = 50
func()
print 'Value of x is', x

#函数func
x = 50
func(x)
print 'x still', x

#函数printMax
printMax(3,4)
x = 5
y = 45
printMax(x,y)



def say(message, times = 1):
    print message * times
say('hello')
say('world ', 5)

def funcx(a, b=5, c=10):
    print 'a is ', a, 'and b is', b, 'and c is',c
funcx(3,7)
funcx(25,c=34)
funcx(c=50,a=100)

def maximum(x,y):
    if x > y:
        return x
    else:
        return y
print maximum(4,5)


import sys
print 'slslsl'
for i in sys.argv:
    print i
print '\n\n the python is\n', sys.path, '\n'

if __name__ == '__main__':
    print 'this program is being run by itself'
else:
    print 'I am being imported from another module'

shoplist = ['apple', 'orange', 'banana', 'mango']
print '清单里有', len(shoplist),'个水果\n'

print '清单里分别是:\n'
i = 1
for item in shoplist:
    print '第',i,'是:',item
    i += 1

shoplist.append('rice')
print '新的清单是:',shoplist

shoplist.sort()
print '按字母顺序排列', shoplist

print '我要买第一个水果', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print '我买:',olditem
print '现在的清单是:',shoplist ,'\n'


zoo = ('wolf', 'elephant', 'penguin')
print '动物园里有',len(zoo),'只动物'
newzoo = ('monkey', 'dolphin', zoo)
print '新的动物园有',len(newzoo),'只动物\n'

print '所有的动物是:', newzoo
print '最后两只动物是什么?', newzoo[2][2]


class Person:

    population = 0

    def __init__(self,name):
        self.name = name
        print '(initializing %s)' % self.name
        Person.population += 1

    def __del__(self):
        print '%s says bye.' % self.name
        Person.population -= 1

        if Person.population == 0:
            print '我是最后一个'
        else:
            print '仍有 %d 个人在左边' % Person.population

    def sayHi(self):
        print '我的名字是:%s.' % self.name

    def howMany(self):
        if Person.population == 1:
            print '我是唯一的人'
        else:
            print '我们有 %d 个人',Person.population

lihao = Person('lihao')
lihao.sayHi()
lihao.howMany()

suona = Person('索呐')
suona.sayHi()
suona.howMany()

junjun = Person('李远钊')
junjun.sayHi()
junjun.howMany()
'''

'''
class JiCheng():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print '(initialed school:)', self.name

    def tell(self):
        print '名字:',self.name,'年龄:',self.age

class Teacher(JiCheng):

    def __init__(self,name,age,salary):
        JiCheng.__init__(self,name,age)
        self.salary = salary
        print '老师名字',self.name

    def tell(self):
        JiCheng.tell(self)
        print 'salary:',self.salary

class Student(JiCheng):

    def __init__(self,name,age,marks):
        JiCheng.__init__(self,name,age)
        self.marks = marks
        print '学生',self.name

    def tell(self):
        JiCheng.tell(self)
        print 'marks:',self.marks

t = Teacher('吴老师', 40, 30000)
s = Student('均均', 22, 75)

members = [t,s]
for member in members:
    member.tell()
'''

pemo = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!'''

f = file('pemo.txt','w')
f.write(pemo)
f.close()

f = file('pemo.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        print line
f.close()

lauda = '''同意。

    彭莹同学在商务采购和供应链谈判方面有非常独特的能力，也有比较好的资源，对各种器件和外围材料的成本都了如指掌，对成本的控制起到了非常重要的作用。
    同时她为人也非常的直率和真诚，在优酷做硬件的早期，这种沟通能力尤为重要，因为信任是合作的基础，她的性格特点、专业素养帮我们在整合外部资源、在推动内部流程、在跨团队协调上起到非常好的推动作用，节省了效率。
    感谢彭莹在一些事务上对我和对团队非常直接的提醒，让我们在早期野蛮生长、快速推进时，克服了总总困扰，依然可以按照公司制度和流程去做事。

    期待彭莹再次回到深圳后可以远离雾霾的困扰，期待你刚出生的孩子可以茁壮成长。'''
f = file('pengying.txt','w')
f.write(lauda)
f.close()

f = file('pengying.txt')
while True:
    line1 = f.readline()
    if len(line1) == 0:
        break
    else:
        print line1

# from collections import Counter
# words = [word for word in jieba.cut(line2, cut_all=True) if len(word) >= 2]
# c = Counter(words)
# for x in c:
#     print x

f.close()