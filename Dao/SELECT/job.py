# coding=utf-8
# table: 'job' 的查询类
from util.DBLink import easy_connect

def CHECK_job_name_EXIST_AND_RETURN_job_id(job_name,handler=None):
    if not handler:
        handler=easy_connect()

    query = "select job_id from job where job_name = %s"
    param = (job_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return False
    else:
        return result[0][0]