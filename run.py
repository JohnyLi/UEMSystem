#!/usr/bin/env python
# coding=utf-8


from flask import Flask, g, session,redirect,url_for
from datetime import timedelta
from service.serviceModule import *
from util.DBLink import *
from conf.Config import *

# 全局配置
# =================================
app=Flask(__name__)
app.config.update(dict(SECRET_KEY=SECRET_KEY,SESSION_COOKIE_HTTPONLY=True))
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# CORS(app, supports_credentials=True) # 允许跨域访问

sqlServer = SQLServer()  # 实例化 SQLServer
sqlServer.start()

# 其他配置
# =================================
@app.before_first_request
def before_first_request():
    pass

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=24)
    if not hasattr(g,'sqlServer'):
        g.sqlServer = sqlServer


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

@app.route(WEB_look+"<year>", methods=['GET'])
def web_look_interface(year):
    return web_lookImpl(year)

@app.route(WEB_student_info,methods=['GET'])
def web_student_info_interface():
    return web_student_infoImpl()




# api
# =================================

# 登录
@app.route(API_login, methods=['POST'])
def api_login_interface():
    return api_loginImpl()



# 返回所有用户信息
@app.route(API_getAllAccountInfo, methods=['POST'])
def api_getAllAccountInfo_interface():
    return api_getAllAccountInfoImpl()

# logout
# =================================
@app.route(URL_LOGOUT)
def logout():
    session.clear()
    return redirect(url_for("web_welcome_interface"))



if __name__ == '__main__':
    Port = 5000
    Host = '0.0.0.0'
    app.run(port=Port,debug=True)
    #app.run(host=Host,port=Port)