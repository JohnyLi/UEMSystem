# coding=utf-8
from flask import render_template,redirect,url_for,session
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from conf.URL_Config import url_dict,STUDENT_BAR
from Dao.SELECT.student import GET_student_INFO_BY_ID
from Dao.SELECT.student_job import *
def web_student_infoImpl():
    if not check_session():
        return redirect(url_for("logout"))
    sidebar = GetSideBar(STUDENT_BAR,"个人信息")
    handler = getSQLHandler()
    id = session['user']
    data = {}
    result = GET_student_INFO_BY_ID(id,handler)

    if result == None:
        return redirect(url_for("logout"))
    else:
        data["name"]=result[1]
        data["id"] = result[0]
        data["gender"] = result[4]
        data["enroll_year"] = result[2]
        data["gradu_year"] = result[3]
        data["status"] = result[5]
        if data['status']!="待业":
            student_job_info = GET_student_job_info_BY_stu_id(id,handler)
            if student_job_info!=None:
                data['company_name'] = student_job_info[6]
                data['job_name'] = student_job_info[3]

    return render_template("student_info.html",sidebar=sidebar,data=data,url_dict=url_dict)