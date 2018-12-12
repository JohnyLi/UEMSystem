# coding=utf-8
from flask import Flask, g,request,render_template,session,redirect
from util.Functions1 import getSQLHandler
from conf.URL_Config import url_dict
from Dao.SELECT.student import GET_ALL_student_INFO_BY_YEAR,GET_ALL_gradu_Year

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
