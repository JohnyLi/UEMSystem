# coding=utf-8
from flask import render_template
from util.Functions1 import getSQLHandler
from conf.URL_Config import url_dict
def web_welcomeImpl():
    handler = getSQLHandler()
    return render_template("welcome.html",url_dict=url_dict)