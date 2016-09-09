#-*- coding:utf-8 -*-

from flask import Flask
lauda = Flask(__name__)
@lauda.route("/")

def hello():
    return "今天不是美好的一天"

if __name__  == "__main__":
    lauda.run()
