from flask import request,jsonify
import json
from startService import getSQLHandler
from util.Sha import *
def getAllAccountInfoImpl():
    response = {}
    handler = getSQLHandler()
    myjson = json.loads(request.get_data().decode())
    name = myjson['name']
    password = myjson['password']
    SHA_PW = get_sha(password)
    result = handler.SELECT("select * from login where name=%s",(name))
    if len(result)==0:
        response['status']="用户名不存在"
    else:
        if SHA_PW==result[0][2]:
            response['status']="登陆成功"
        else:
            response['status']="密码错误"
    return jsonify(response)
