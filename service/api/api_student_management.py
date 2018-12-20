from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from Dao.SELECT.major_student import GET_ALL_STUDENT_INFOS
from conf.Config import *
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
    elif control=="add":



    return jsonify(response1)




