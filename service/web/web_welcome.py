# coding=utf-8
from flask import render_template,session,redirect,url_for
from util.Functions1 import getSQLHandler,check_session
from conf.URL_Config import url_dict
from conf.Global_Config import *
def web_welcomeImpl():
    if check_session():
        privilege = session['privilege']
        if privilege == PRIVILEGE_STUDENT:
            return redirect(url_for("web_student_info_interface"))
        elif privilege == PRIVILEGE_ADMIN:
            return redirect(url_for("web_admin_info_interface"))
    return render_template("welcome.html",url_dict=url_dict)