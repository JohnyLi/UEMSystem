# coding=utf-8
# table: 'com_job' 的更新类
from util.DBLink import easy_connect
from util.Time import *
def NEW_com_job(com_id,job_id,need_num,end_date,style_id,handler=None):
    if not handler:
        handler=easy_connect()

    query = "insert into com_job (com_id,job_id,need_num,start_time,finish_time,style_id) values (%s,%s,%s,%s,%s,%s)"
    param = (com_id,job_id,need_num,from_year_to_day(),end_date,style_id)
    return handler.UPDATE(query,param)


def UPDATE_com_job(com_job_id,com_id,need_num,end_date,style_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "update com_job set com_id=%s,need_num=%s,finish_time=%s,style_id=%s where com_job_id=%s"
    param = (com_id,need_num,end_date,style_id,com_job_id)
    return handler.UPDATE(query, param)



