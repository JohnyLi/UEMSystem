# coding=utf-8
from flask import render_template,redirect,url_for,session,request
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from Dao.SELECT.student import GET_student_INFO_BY_ID
from Dao.SELECT.com_job import GET_com_job_BY_com_id
from Dao.SELECT.com_job import GET_ALL_com_nameandid
from conf.Config import *
def web_student_registerImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_STUDENT:
        return redirect(url_for("logout"))

    sidebar = GetSideBar(STUDENT_BAR, "就业登记")
    handler = getSQLHandler()
    id = session['user']

    company_id = int(request.args.get("com_id",1))

    data = {}
    result1 = GET_student_INFO_BY_ID(id, handler)

    if result1 == None:
        return redirect(url_for("logout"))
    else:
        data["name"] = result1[1]
        data["id"] = result1[0]
        data["gradu_year"] = result1[3]

    companies = []
    company_info=GET_ALL_com_nameandid(handler)
    for i in company_info:
        temp = {}
        temp['id']=i[0]
        temp['name']=i[1]
        companies.append(temp)

    company_job = []
    com_job_infos = GET_com_job_BY_com_id(company_id,handler)
    for com_job_info in com_job_infos:
        temp = {}
        temp['com_name']=com_job_info[7]
        temp['job_name'] = com_job_info[8]
        temp['need_num'] = com_job_info[4]
        temp['exist_num'] = com_job_info[3]
        temp['start_time'] = com_job_info[5]
        temp['finish_time'] = com_job_info[6]
        temp['com_job_id'] = com_job_info[0]
        company_job.append(temp)


    return render_template("student_register.html",now_com_id = company_id,
                           sidebar=sidebar, data=data, url_dict=url_dict, companies=companies,company_job = company_job)

