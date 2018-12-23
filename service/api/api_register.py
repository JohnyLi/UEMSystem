from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from Dao.SELECT.verify import CHECK_EXIST
from Dao.UPDATE.verify import INSERT_NEW_register
from Dao.SELECT.com_job import CHECK_com_job_NUM_NOT_ENOUGH
from conf.Config import *
def api_registerImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_STUDENT or not check_session():
        return
    response1 = {}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))

    user = session['user']
    com_job_id = data['com_job_id']
    if CHECK_EXIST(user,handler):
        response1['status']="不可二次登记"
    else:
        if CHECK_com_job_NUM_NOT_ENOUGH(com_job_id):
            if INSERT_NEW_register(com_job_id,user,handler):
                response1['status'] = "登记成功，待审核"
            else:
                response1['status'] = "登记失败，请重新登记"
        else:
            response1['status']="该职位人数已满"


    return jsonify(response1)
