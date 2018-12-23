# coding=utf-8
from flask import render_template,redirect,url_for,session
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from conf.Config import *
from Dao.SELECT.company import *
from Dao.SELECT.job_style import *
def web_company_managementImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN:
        return redirect(url_for("logout"))

    sidebar = GetSideBar(ADMIN_BAR,"公司招聘信息")
    handler = getSQLHandler()

    style_infos = GET_ALL_style_infos(handler)
    com_infos = GET_ALL_company_infos(handler)

    return render_template("company_management.html", sidebar=sidebar, url_dict=url_dict,
                           style_infos=style_infos,com_infos=com_infos)