# coding=utf-8
# table: 'major_apart' 的查询类

from util.DBLink import easy_connect
def GET_ALL_apart_infos(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from apartment"
    param = ()
    result = handler.SELECT(query,param)
    return result

def GET_ALL_major_infos(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from v_apart_major"
    result = handler.SELECT(query)
    return result