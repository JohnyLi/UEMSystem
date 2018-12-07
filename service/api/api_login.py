
from flask import jsonify,request
import json
from startService import getSQLHandler 
from Dao import *
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
    result=CHECK_user_name_AND_password(user_name,password,handler)
    if result:
        response1['status']='success'
    else:
        response1['status'] = 'fail'

    return jsonify(response1)