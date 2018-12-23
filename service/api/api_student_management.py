from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from Dao.SELECT.major_student import *
from Dao.UPDATE.major_student import *
from Dao.UPDATE.student import *
from Dao.SELECT.student import *
from conf.Config import *
from Dao.UPDATE.verify import *
from Dao.SELECT.student_job import *
from Dao.UPDATE.student_job import *
from Dao.SELECT.com_job import *
def api_student_managementImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN or not check_session():
        return
    response1 = {'status':""}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    control = data['control']

    if control == "get_student_info":
        student_infos = GET_ALL_STUDENT_INFOS(handler)
        if student_infos:
            result = []
            for info in student_infos:
                temp = {}
                temp['stu_id'] = info[0]
                temp['stu_name'] = info[1]
                temp['gender'] = info[4]
                temp['enroll_year'] = info[2]
                temp['gradu_year'] = info[3]
                temp['status'] = info[5]
                temp['major_name'] = info[8]
                result.append(temp)
            response1['status']="success"
            response1['data']=result
        else:
            response1['status']="fail"
    elif control=="get_com_job_infos":
        com_job_infos = GET_ALL_com_job_infos(handler)
        if com_job_infos != None:
            response1['data'] = com_job_infos
            response1['status'] = "success"
        else:
            response1['status'] = 'fail'

    elif control=="add" or control=="change":
        stu_id = data['stu_id']
        stu_name = data['stu_name']
        gender = data['gender']
        enroll_year = data['enroll_year']
        gradu_year = data["gradu_year"]
        major_name = data['major_name']
        stu_exist = GET_major_id_BY_stu_id(stu_id,handler)
        if control=="add":
            if stu_exist:
                response1['status']="用户已存在"
            else:
                status = ADD_NEW_STUDENT(stu_id,stu_name,gender,enroll_year,gradu_year,handler)
                if not status:
                    response1['status']="新建失败"
                else:
                    status = INSERT_NEW_major_student(major_name,stu_id,handler)
                    if not status:
                        response1['status'] = "新建失败"
                    else:
                        response1['status'] = "新建成功"
        elif control=="change":
            if not stu_exist:
                response1['status']="用户不存在"
            else:
                status = UPDATE_STUDENT(stu_id,stu_name,gender,enroll_year,gradu_year,handler)
                if not status:
                    response1['status'] = "更新失败"
                else:
                    status = UPDATE_major_student(major_name,stu_id,handler)
                    if not status:
                        response1['status'] = "更新失败"
                    else:
                        response1['status'] = "更新成功"
    elif control=="delete":
        stu_id = data['stu_id']
        stu_exist = GET_major_id_BY_stu_id(stu_id,handler)
        if not stu_exist:
            response1['status']="用户不存在"
        else:
            status = DELETE_major_student(stu_id,handler)
            status = status and DELETE_student_IN_student_job(stu_id,handler)
            status = status and DELETE_student_IN_verify(stu_id,handler)
            status = status and DELETE_STUDENT(stu_id, handler)
            if not status:
                response1['status'] = "删除失败"
            else:
                response1['status'] = "删除成功"
    elif control=="reset":
        stu_id = data['stu_id']
        stu_exist = GET_major_id_BY_stu_id(stu_id, handler)
        if not stu_exist:
            response1['status'] = "用户不存在"
        else:
            status = CHANGE_STUDENT_password(stu_id,Default_password,handler)
            if not status:
                response1['status']="重置失败"
            else:
                response1['status']="重置成功"

    elif control == "register":
        com_job_id = data['com_job_id']
        stu_id = data['stu_id']
        if CHECK_student_pass_or_not(stu_id, handler):
            response1['status']="学生已就业"
        else:
            if CHECK_com_job_NUM_NOT_ENOUGH(com_job_id,handler):
                result = INSERT_NEW_student_job(stu_id, com_job_id, handler)  # 插入student_job表
                verify_id = INSERT_NEW_register_AND_RETURN_verify_id(com_job_id,stu_id)
                result = result and UPDATE_register(verify_id, STATUS_PASS, handler)  # 更改登记状态
                result = result and REFRESH_student_status(stu_id, handler)  # 刷新学生就业状态
                if result:
                    response1['status']="登记成功"
                else:
                    response1['status']="登记失败"
            else:
                response1['status']="该职位需求人数已满"

    return jsonify(response1)




