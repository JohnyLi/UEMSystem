# coding=utf-8
# table: 'admin' 的更新类


from util.Sha import get_sha
from Dao.SELECT.admin import CHECK_USER_IS_EXIST,GET_USER_ID
from util.DBLink import easy_connect
def INSERT_A_NEW_USER(user_name,password,handler=None):
    """
    插入一个新的用户
    :param user_name: str
    :param password: str
    :param handler: SQLServer
    :return: bool
    """
    if not handler:
        handler=easy_connect()
    if CHECK_USER_IS_EXIST(user_name,handler):
        return False
    query = "insert into admin (user_name,password) value(%s,%s)"
    param = (user_name, get_sha(password))
    return handler.UPDATE(query, param)

def UPDATE_USER_INFO(user_name,password,handler=None):
    """
    更新用户名或密码
    :param user_name: str
    :param password: str
    :param handler: SQLServer
    :return: bool
    """
    if not handler:
        handler=easy_connect()
    if CHECK_USER_IS_EXIST(user_name,handler):
        return False
    user_id = GET_USER_ID(user_name,handler)
    query = "update admin set user_name=%s,password=%s where user_id=%s"
    param = (user_name, get_sha(password), user_id)
    return  handler.UPDATE(query, param)


def DELETE_USER(user_name,handler=None):
    """

    :param user_name:
    :param handler:
    :return:
    """
    if not handler:
        handler=easy_connect()
    query="delete from %s where user_name=%s "
    param=(user_name)
    return handler.UPDATE(query,param)

def CHANGE_ADMIN_password(user_name,password,handler=None):

    if not handler:
        handler=easy_connect()
    query = "update admin set password=%s where user_name=%s"
    param = ( get_sha(password), user_name)
    return  handler.UPDATE(query, param)