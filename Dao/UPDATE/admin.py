# coding=utf-8
# table: 'user' 的更新类


from util.Sha import get_sha
from Dao.SELECT.admin import CHECK_USER_IS_EXIST,GET_USER_ID
from public.DBLink import easy_connect
from conf import *
def INSERT_A_NEW_USER(user_name,password,handler=easy_connect()):
    """
    插入一个新的用户
    :param user_name: str
    :param password: str
    :param handler: SQLServer
    :return: bool
    """
    if CHECK_USER_IS_EXIST(user_name,handler):
        return False
    query = "insert into %s (user_name,password) value(%s,%s)"
    param = (TABLE_admin, user_name, get_sha(password))
    return handler.UPDATE(query, param)

def UPDATE_USER_INFO(user_name,password,handler=easy_connect()):
    """
    更新用户名或密码
    :param user_name: str
    :param password: str
    :param handler: SQLServer
    :return: bool
    """
    if CHECK_USER_IS_EXIST(user_name,handler):
        return False
    user_id = GET_USER_ID(user_name,handler)
    query = "update %s set user_name=%s,password=%s where user_id=%s"
    param = (TABLE_admin, user_name, get_sha(password), user_id)
    return  handler.UPDATE(query, param)


def DELETE_USER(user_name,handler=easy_connect()):
    """

    :param user_name:
    :param handler:
    :return:
    """
    query="delete from %s where user_name=%s "
    param=(TABLE_admin, user_name)
    return handler.UPDATE(query,param)
