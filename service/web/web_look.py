# coding=utf-8
from flask import Flask, g,request,render_template,session,redirect
from util.Functions1 import getSQLHandler
from conf.URL_Config import url_dict
from Dao.SELECT.student import GET_ALL_student_INFO_BY_YEAR,GET_ALL_gradu_Year
from Dao.SELECT.major import GET_ALL_major,GET_major_name_BY_major_id
from Dao.SELECT.major_student import GET_major_id_BY_stu_id
def web_lookImpl(year):
    handler = getSQLHandler()
    years = GET_ALL_gradu_Year(handler)
    year = int(year)
    if year not in years:
        year = years[0]
    infos = GET_ALL_student_INFO_BY_YEAR(year,handler)

    result = get_employ_con(infos)
    return render_template("look.html",result=result,years=years,url_dict=url_dict)


def get_employ_con(infos):
    result = {'gradu_num':len(infos),'employ_num':0,'wait_num':0}
    for info in infos:
        if info[5]=='待业':
            result['wait_num']+=1
        else:
            result['employ_num']+=1

    result['employ_rate']=str(result['employ_num']/result['gradu_num']*100)+'%'
    return result

def get_employ_con_major(handler,infos):
    student_id_list = []
    major_infos = {}
    for i in infos:
        student_id_list.append((i[0],i[5]))
    for stu in student_id_list:
        stu_id = stu[0]
        stu_state = stu[1]
        major_id = GET_major_id_BY_stu_id(stu_id,handler)
        major_name = GET_major_name_BY_major_id(major_id,handler)


