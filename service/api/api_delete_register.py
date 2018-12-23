from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from conf.Config import *
from Dao.SELECT.verify import *
from Dao.UPDATE.verify import *

def api_delete_registerImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_STUDENT or not check_session():
        return
    response1 = {}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    verify_id = data['verify_id']
    status = GET_verify_status_BY_verify_id(verify_id)
    if status!=STATUS_WAITING:
        response1['status']="无法删除"
    else:
        if DELETE_student_IN_verify(verify_id,handler):
            response1['status']="删除成功"
        else:
            response1['status']="删除失败"

    return jsonify(response1)