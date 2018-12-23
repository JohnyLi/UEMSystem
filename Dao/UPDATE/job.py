# coding=utf-8
# table: 'job' 的更新类
from util.DBLink import easy_connect

def NEW_job_AND_RETURN_job_id(job_name,handler=None):
    if not handler:
        handler=easy_connect()

    query = "insert into job (job_name) values (%s)"
    param = (job_name)
    handler.UPDATE(query,param)
    query = "select max(job_id) from job"
    result = handler.SELECT(query)
    return result[0][0]

