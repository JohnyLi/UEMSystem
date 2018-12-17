
from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler
from Dao.SELECT.admin import CHECK_user_name_AND_password
from Dao.SELECT.student import CHECK_stu_id_AND_password
from conf.Config import *
def api_loginImpl():
    """
    :INPUT: {'user_name':<user_name> -> str ,'password':<password> -> str}
    :return: {'status': 'success'} or {'status': 'fail'}
    """
    response1 = {}
    handler = getSQLHandler()   # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data['user_name']
    password=data['password']
    result=loginCheck(user_name,password,handler)
    if result:
        response1['status'] = 'success'
        response1['privilege'] = result
        session['privilege'] = result
        session['id'] = user_name
    else:
        response1['status'] = 'fail'
        session.clear()

    return jsonify(response1)

def loginCheck(user_name,password,handler):
    if CHECK_user_name_AND_password(user_name, password, handler):
        return PRIVILEGE_ADMIN
    elif CHECK_stu_id_AND_password(user_name,password,handler):
        return PRIVILEGE_STUDENT
    else:
        return False