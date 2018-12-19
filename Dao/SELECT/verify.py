# coding=utf-8
# table: 'verify' 的查询类

from util.DBLink import easy_connect
from conf.Config import *
def CHECK_EXIST(stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from verify where stu_id=%s"
    param = (stu_id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        for row in result:
            if row[3]==STATUS_WAITING or row[3]==STATUS_SUCCESS:
                return True
        return False
def GET_VERIFY_INFOS_BY_stu_id(stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from v_verify_com_job where stu_id=%s"
    param = (stu_id)
    result = handler.SELECT(query,param)
    return result