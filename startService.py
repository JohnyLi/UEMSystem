#!/usr/bin/env python
# coding=utf-8


from flask import Flask, g,request,render_template,session,redirect
from flask_cors import CORS
from datetime import timedelta

from service import *
from conf import *
from public.DBLink import *



# 全局配置
# =================================
app=Flask(__name__)
app.config.update(dict(SECRET_KEY=SECRET_KEY))
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# CORS(app, supports_credentials=True) # 允许跨域访问

sqlServer = SQLServer()  # 实例化 SQLServer

# 其他配置
# =================================
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=24)

def getSQLHandler():
    if not hasattr(g, 'handler'):
        conn = sqlServer.getConn()
        g.handler = SQLHandler(conn)

    return g.handler

@app.teardown_appcontext    #用户访问结束后，关闭database连接，释放资源
def close_handler(error):
    if hasattr(g, 'handler'):
        g.handler.close()

# web
# =================================

# 欢迎界面
@app.route(WEB_welcome, methods=['GET'])
def web_welcome_interface():
    return web_welcomeImpl()




# api
# =================================

# 登录
@app.route(API_login, methods=['POST'])
def api_login_interface():
    return api_getAllAccountInfoImpl()



# 返回所有用户信息
@app.route(API_getAllAccountInfo, methods=['POST'])
def api_getAllAccountInfo_interface():
    return api_getAllAccountInfoImpl()




if __name__ == '__main__':
    sqlServer.start()
    app.run(port=5000,debug=True)