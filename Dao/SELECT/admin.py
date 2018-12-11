# coding=utf-8
# table: 'user' 的查询类


from util.Sha import get_sha
from util.DBLink import easy_connect
def CHECK_user_name_AND_password(user_name,password,handler=None):
    """
    检查用户名和密码的正确与否
    :param user_name: str
    :param password: str
    :param handler: SQLHandler
    :return: bool
    """
    if not handler:
        handler=easy_connect()
    query = "select password from admin where user_name = %s"
    param = (user_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        Sha_password = get_sha(password)
        if Sha_password == result[0][0]:
            return True
        else:
            return False

def CHECK_USER_IS_EXIST(user_name,handler=None):
    """
    检查某个用户名是否存在
    :param user_name: str
    :param handler: SQLHandler
    :return: bool
    """
    if not handler:
        handler=easy_connect()
    query = "select * from admin where user_name = %s"
    param = (user_name)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return False
    else:
        return True

def GET_USER_ID(user_name,handler=None):
    """
    获取用户名对应的id
    :param user_name: str
    :param handler: SQLHandler
    :return: None or int
    """
    if not handler:
        handler=easy_connect()
    query = "select user_id from admin where user_name = %s"
    param = (user_name)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return None
    else:
        return result[0][0]