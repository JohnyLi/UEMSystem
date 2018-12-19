# coding=utf-8
from flask import render_template,redirect,url_for,session
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from conf.Config import *
from Dao.SELECT.major import GET_ALL_major_INFOS
def web_student_managementImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN:
        return redirect(url_for("logout"))

    sidebar = GetSideBar(ADMIN_BAR,"学生管理")
    handler = getSQLHandler()
    majors = GET_ALL_major_INFOS(handler)
    return render_template("student_management.html",sidebar=sidebar,url_dict=url_dict,majors=majors)