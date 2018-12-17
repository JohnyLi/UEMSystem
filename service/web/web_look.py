# coding=utf-8
from flask import request,render_template,session
from util.Functions1 import getSQLHandler
from conf.URL_Config import url_dict
from Dao.SELECT.student import GET_ALL_student_INFO_BY_YEAR,GET_ALL_gradu_Year
from Dao.SELECT.major import GET_ALL_major_INFOS
from Dao.SELECT.major_student import GET_ALL_major_student_INFOS
from util.Time import get_year

def web_lookImpl():
    handler = getSQLHandler()   #  获取handler
    privilege = session.get("privilege")    #  获取session中的权限，如果不存在该privilege则为None

    gradu_years = GET_ALL_gradu_Year(handler)     #  获取所有毕业年份
    now_year = int(request.args.get("year",get_year()))     #  获取url中的毕业年份
    if now_year not in gradu_years:
        now_year = gradu_years[0]

    infos = GET_ALL_student_INFO_BY_YEAR(now_year,handler)  #  通过毕业年份获取学生信息
    head = get_total_employ_con(infos)
    data = get_employ_con_major(handler,infos)

    return render_template("look.html",head=head,privilege=privilege,
                           years=gradu_years,url_dict=url_dict,data=data,now_year = now_year)


def get_total_employ_con(infos):
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
    major_student_dict = {}
    major_student_infos = GET_ALL_major_student_INFOS(handler)
    major_infos = GET_ALL_major_INFOS(handler)
    for i in infos:
        student_id_list.append((i[0],i[5]))
    for stu in student_id_list:
        stu_id = stu[0]
        stu_state = stu[1]
        for major_student_info in major_student_infos:
            if major_student_info[0]==stu_id:
                major_id = major_student_info[1]
                break
        for major_info in major_infos:
            if major_info[0]==major_id:
                major_name = major_info[1]
                break
        if major_student_dict.__contains__(major_name):
            major_student_dict[major_name]['major_num']+=1
            if stu_state=='待业':
                major_student_dict[major_name]['major_wait_num']+=1
            else:
                major_student_dict[major_name]['major_employ_num'] += 1
        else:
            major_student_dict[major_name]={'major_num':0,'major_wait_num':0,'major_employ_num':0}

    result = []
    for major_name in major_student_dict.keys():
        temp = {"major_name":major_name}
        temp['major_wait_num'] = major_student_dict[major_name]['major_wait_num']
        temp['major_num'] = major_student_dict[major_name]['major_num']
        temp['major_employ_num'] = major_student_dict[major_name]['major_employ_num']
        try:
            temp['major_employ_rate'] = str(temp['major_employ_num']/temp['major_num']*100)+"%"
        except:
            temp['major_employ_rate'] = "NaN"
        result.append(temp)
    return result
