from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from conf.Config import *
from Dao.SELECT.verify import *
from Dao.UPDATE.verify import *
from Dao.SELECT.student_job import *
from Dao.UPDATE.student_job import *
from Dao.SELECT.com_job import *
def api_register_checkImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN or not check_session():
        return
    response1 = {}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    control = data['control']
    if control == "get_register":
        result = GET_ALL_verify_INFOS(handler)
        response1['data'] =result
        response1['status']= "success"
    elif control == STATUS_PASS :
        verify_id = data['verify_id']
        stu_id = data['stu_id']
        com_job_id = data['com_job_id']
        # 若学生未被审批通过
        if not CHECK_student_pass_or_not(stu_id,handler):
            if CHECK_com_job_NUM_NOT_ENOUGH(com_job_id, handler):
                result = INSERT_NEW_student_job(stu_id, com_job_id, handler)  # 插入student_job表
                result = result and UPDATE_register(verify_id, control, handler) #更改登记状态
                result = result and REFRESH_student_status(stu_id,handler) #刷新学生就业状态
                if result:
                    response1['status'] = "操作成功"
                else:
                    response1['status'] = "操作失败"
            else:
                response1['status']="该职位需求人数已满"
        else:
            response1['status'] = "学生已就业"

    elif control == STATUS_WAITING:
        verify_id = data['verify_id']
        stu_id = data['stu_id']
        com_job_id = data['com_job_id']

        # 若学生未被审批通过
        if not CHECK_student_pass_or_not(stu_id, handler):
            result = UPDATE_register(verify_id, control, handler) #更改登记状态
            if result:
                response1['status'] = "操作成功"
            else:
                response1['status'] = "操作失败"

        # 若学生已审核通过
        else:
            result = DELETE_student_job(stu_id, com_job_id, handler)  # 插入student_job表
            result = result and UPDATE_register(verify_id, control, handler)  # 更改登记状态
            result = result and REFRESH_student_status(stu_id, handler)  # 刷新学生就业状态
            if result:
                response1['status'] = "操作成功"
            else:
                response1['status'] = "操作失败"

    elif control == STATUS_FAIL:
        verify_id = data['verify_id']
        result = UPDATE_register(verify_id, control, handler)  # 更改登记状态
        if result:
            response1['status'] = "操作成功"
        else:
            response1['status'] = "操作失败"


    return jsonify(response1)