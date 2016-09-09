#-*- coding:utf-8 -*-
from flask import Flask,render_template
from models import User
from modelsRace import Race
import torndb
app = Flask(__name__)

@app.route("/")
def index():
    return 'hello world'

@app.route("/Users/lihao")
def xuexi():
    return u'sina.com.cn'

@app.route("/pic/<name>")
def pic(name):
    return u'my name is:%s' % name

@app.route("/table")
def testTable():
    return render_template('table.html')

@app.route("/picc/<pages>")
def yeshuo(pages):
    return u'这是第' + pages + u'页'

@app.route("/page/<pages>/total/<total>")
def totalpage(pages, total):
    return u'总共有'+ pages + u'页' + u'这是第' + total + u'页'

@app.route("/template1")
def testemp():
    title = u'test demo'
    name = 'liyuanzhao'
    pages = {'page': '10', 'total': '20'}
    content = "this is flask demo of use template!!!!!"
    return render_template('template1.html', title=title, name=name, pages=pages, content=content)


@app.route("/user_index")
def user_index():
    user = User(1,'-----lauuuuddddaa')
    return render_template('user_index.html', user=user)

@app.route("/qurey_user/<user_id>")
def qurey_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'today is googd news')
    return render_template("user_id.html",user=user)

#模板的页面遍历与循环
@app.route("/user_list")
def user_list():
    lauda = []
    for i in range(1, 20):
        lau = User(i, 'lihao' + str(i))
        lauda.append(lau)
    return render_template("user_list.html", users=lauda)

#模板的继承
@app.route("/one")
def one_base():
    user = User(1, '-----lauuuuddddaa')
    return render_template("one_base.html",user=user)

#模板的继承
@app.route("/two")
def two_base():
    lauda = []
    for i in range(1, 20):
        lau = User(i, 'lihao' + str(i))
        lauda.append(lau)
    return render_template("two_base.html", users=lauda)


@app.route("/raceTable")
def tableRace():

    race = []

    db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceAJS"):
        print u'NAMA:', raceInfo.raceName
        print u'ADD:', raceInfo.raceADD
        print u'TIME:', raceInfo.raceTime
        print u'NOTE:', raceInfo.raceNote

        raceCon = Race(raceInfo.raceName, raceInfo.raceADD, raceInfo.raceTime, raceInfo.raceNote)
        race.append(raceCon)
    return render_template("raceTable.html", ajs=race)

if __name__ == '__main__':
    app.run(debug=True)