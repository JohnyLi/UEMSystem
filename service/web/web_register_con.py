# coding=utf-8
from flask import render_template,redirect,url_for,session,request
from util.Functions1 import getSQLHandler,GetSideBar,check_session
from Dao.SELECT.student import GET_student_INFO_BY_ID
from Dao.SELECT.com_job import GET_com_job_BY_com_id
from Dao.SELECT.com_job import GET_ALL_com_nameandid
from Dao.SELECT.verify import GET_VERIFY_INFOS_BY_stu_id
from conf.Config import *
def web_register_conImpl():
    if not check_session():
        return redirect(url_for("logout"))
    privilege = session['privilege']
    if privilege != PRIVILEGE_STUDENT:
        return redirect(url_for("logout"))
    sidebar = GetSideBar(STUDENT_BAR, "审核状态")
    handler = getSQLHandler()
    user = session['user']

    infos = GET_VERIFY_INFOS_BY_stu_id(user,handler)
    company_job = []
    for info in infos:
        temp ={}
        temp['verify_id']=info[0]
        temp['com_name']=info[11]
        temp['job_name']=info[12]
        temp['register_time']=info[4]
        temp['verify_con']=info[3]
        company_job.append(temp)

    return render_template("register_con.html", company_job = company_job,
                           sidebar=sidebar,url_dict=url_dict)


