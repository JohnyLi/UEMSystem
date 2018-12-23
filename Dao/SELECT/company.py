# coding=utf-8
# table: 'company' 的查询类
from util.DBLink import easy_connect

def CHECK_com_name_exist(com_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from company where com_name = %s"
    param = (com_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        return True


def GET_ALL_company_infos(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from company"
    return handler.SELECT(query)