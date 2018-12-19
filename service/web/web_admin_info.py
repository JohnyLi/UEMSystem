# coding=utf-8
from flask import render_template,redirect,url_for,session
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from conf.Config import *
def web_admin_infoImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN:
        return redirect(url_for("logout"))

    sidebar = GetSideBar(ADMIN_BAR,"个人信息")
    handler = getSQLHandler()
    user = session['user']
    return render_template("admin_info.html",sidebar=sidebar,url_dict=url_dict,user=user)