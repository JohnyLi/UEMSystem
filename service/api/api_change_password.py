from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from Dao.SELECT.admin import CHECK_user_name_AND_password
from Dao.SELECT.student import CHECK_stu_id_AND_password
from Dao.UPDATE.student import CHANGE_STUDENT_password
from Dao.UPDATE.admin import CHANGE_ADMIN_password
from conf.Config import *
def api_change_passwordImpl():
    """
    :INPUT: {'user':<user> -> str ,'old_password':<old_password> -> str, 'new_password':<new_password> -> str}
    :return: {'status': '旧密码错误'} or {'status': '修改成功'} or {'status': '修改失败'} or {'status': '请刷新浏览器'}
    """
    response1 = {}
    if check_session():

        handler = getSQLHandler()   # 获取sql连接
        data = json.loads(request.get_data().decode('utf-8'))
        user = data['user']
        old_password = data['old_password']
        new_password = data['new_password']
        result=loginCheck(user,old_password,handler)
        if result:
            if result == PRIVILEGE_ADMIN:
                if CHANGE_ADMIN_password(user, new_password, handler):
                    response1['status'] = '修改成功'
                else:
                    response1['status'] = '修改失败'
            elif result == PRIVILEGE_STUDENT:
                if CHANGE_STUDENT_password(user, new_password, handler):
                    response1['status'] = '修改成功'
                else:
                    response1['status'] = '修改失败'

        else:
            response1['status'] = '旧密码错误'
    else:
        response1['status']="请刷新浏览器"

    return jsonify(response1)

def loginCheck(user_name,password,handler):
    if CHECK_user_name_AND_password(user_name, password, handler):
        return PRIVILEGE_ADMIN
    elif CHECK_stu_id_AND_password(user_name,password,handler):
        return PRIVILEGE_STUDENT
    else:
        return False