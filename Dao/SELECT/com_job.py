# coding=utf-8
# table: 'com_job' 的查询类
from util.Time import *
from util.DBLink import easy_connect
def GET_ALL_com_job_infos(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from v_com_job"
    param = ()
    result = handler.SELECT(query,param)
    return result


def GET_com_job_BY_com_id(com_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from v_com_job where com_id=%s"
    param = (com_id)
    result = handler.SELECT(query,param)
    newReulst = []
    for row in result:
        finishtime = row[6]
        starttime = row[5]
        now_time = time.time()
        if now_time > get_unix_time_by_date(starttime) and now_time < get_unix_time_by_date(finishtime):
            newReulst.append(row)
    return newReulst

def GET_ALL_com_nameandid(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from company"
    result = handler.SELECT(query)
    return result