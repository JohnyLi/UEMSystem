# coding=utf-8
from flask import render_template,session,redirect,url_for
from util.Functions1 import getSQLHandler,check_session,GetSideBar
from conf.Config import *
def web_change_passwordImpl():
    if not check_session():
        return redirect(url_for("logout"))
    user = session['user']
    privilege = session["privilege"]
    if privilege == PRIVILEGE_STUDENT:
        sidebar = GetSideBar(STUDENT_BAR)
    elif privilege == PRIVILEGE_ADMIN:
        sidebar = GetSideBar(ADMIN_BAR)
    else:
        return redirect(url_for("logout"))
    return render_template("change_password.html",url_dict=url_dict, sidebar=sidebar ,user=user)