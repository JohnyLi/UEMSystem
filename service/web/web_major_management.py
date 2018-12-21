# coding=utf-8
from flask import render_template,redirect,url_for,session
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from conf.Config import *
from Dao.SELECT.major_apart import GET_ALL_apart_infos,GET_ALL_major_infos

def web_major_managementImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN:
        return redirect(url_for("logout"))

    sidebar = GetSideBar(ADMIN_BAR,"专业管理")
    handler = getSQLHandler()

    apart_infos = GET_ALL_apart_infos(handler)
    major_infos = GET_ALL_major_infos(handler)

    major_infos_result = []
    for major_info in major_infos:
        temp = {}
        temp['major_id']=major_info[0]
        temp['major_name'] = major_info[1]
        temp['major_num'] = major_info[2]
        temp['apart_name'] = major_info[4]
        major_infos_result.append(temp)

    return render_template("major_management.html",sidebar=sidebar,url_dict=url_dict,
                           apart_infos=apart_infos,data=major_infos_result)