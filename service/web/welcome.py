# coding=utf-8
from flask import Flask, g,request,render_template,session,redirect
from startService import getSQLHandler
from conf.URL_Config import url_dict
def welcomeImpl():
    result = getSQLHandler().SELECT("select * from test")

    return render_template("welcome.html",content = str(result),url_dict = url_dict)