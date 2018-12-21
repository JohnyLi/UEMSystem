# coding=utf-8
# table: 'apartment' 的查询类

from util.DBLink import easy_connect

def CHECK_apart_name_EXIST(apart_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from apartment where apart_name=%s"
    param = (apart_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        return True