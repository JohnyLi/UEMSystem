# coding=utf-8
# table: 'company' 的更新类
from util.DBLink import easy_connect
def NEW_company(com_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into company (com_name) values (%s)"
    param = (com_name)
    return handler.UPDATE(query, param)