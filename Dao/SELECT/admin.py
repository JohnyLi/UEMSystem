# coding=utf-8
# table: 'user' 的查询类


from util.Sha import get_sha
from public.DBLink import easy_connect
from conf import *
def CHECK_user_name_AND_password(user_name,password,handler=easy_connect()):
    """
    检查用户名和密码的正确与否
    :param user_name: str
    :param password: str
    :param handler: SQLHandler
    :return: bool
    """

    query = "select password from %s where user_name = %s"
    param = (TABLE_admin, user_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        Sha_password = get_sha(password)
        if Sha_password == result[0][0]:
            return True
        else:
            return False

def CHECK_USER_IS_EXIST(user_name,handler=easy_connect()):
    """
    检查某个用户名是否存在
    :param user_name: str
    :param handler: SQLHandler
    :return: bool
    """
    query = "select * from %s where user_name = %s"
    param = (TABLE_admin, user_name)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return False
    else:
        return True

def GET_USER_ID(user_name,handler=easy_connect()):
    """
    获取用户名对应的id
    :param user_name: str
    :param handler: SQLHandler
    :return: None or int
    """
    query = "select user_id from %s where user_name = %s"
    param = (TABLE_admin, user_name)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return None
    else:
        return result[0][0]