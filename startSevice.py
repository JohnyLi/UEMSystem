#!/usr/bin/env python
#coding=utf-8

from conf import *
from flask import Flask, g,request,render_template,session,redirect
from flask_cors import CORS
from service import *

##### 全局配置
##### =================================
app=Flask(__name__)
app.config.update(dict(SECRET_KEY=SECRET_KEY))
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
CORS(app, supports_credentials=True)


##### web
##### =================================
@app.route(WEB_welcome, methods=['GET'])
def web_welcome():
    return welcomeImpl()




##### api
##### =================================
@app.route(API_getAllAccountInfo, methods=['POST'])
def api_getAllAccountInfo():
    return getAllAccountInfoImpl()




if __name__ == '__main__':
    app.run(port=5000,debug=True)