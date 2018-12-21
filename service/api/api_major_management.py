from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from conf.Config import *
from Dao.SELECT.apartment import *
from Dao.UPDATE.apartment import *
from Dao.SELECT.major import *
from Dao.UPDATE.major import *
from Dao.UPDATE.major_apart import *
def api_major_managementImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN or not check_session():
        return
    response1 = {'status': ""}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    control = data['control']

    if control == "AddApart":
        apart_name = data['apart_name']
        if CHECK_apart_name_EXIST(apart_name,handler):
            response1['status']="院系名已存在"
        else:
            if ADD_NEW_apartment(apart_name,handler):
                response1['status']="添加成功"
            else:
                response1['status']="添加失败"

    elif control == "AddMajor":
        major_name = data['major_name']
        apart_id = data['apart_id']
        if CHECK_major_name_EXIST(major_name, handler):
            response1['status'] = "专业名已存在"
        else:
            if ADD_NEW_major(major_name, handler):
                major_id = GET_major_id_BY_major_name(major_name, handler)
                if ADD_NEW_apart_major(major_id, apart_id, handler):
                    response1['status'] = "添加成功"
                else:
                    response1['status'] = "添加失败"
            else:
                response1['status'] = "添加失败"



    return jsonify(response1)

