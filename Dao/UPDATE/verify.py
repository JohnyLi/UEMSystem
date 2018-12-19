# coding=utf-8
# table: 'verify' 的更新类
from util.DBLink import easy_connect
from conf.Config import *
def INSERT_NEW_register(com_job_id,stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into verify (com_job_id,stu_id,status) values(%s,%s,%s)"
    param = (com_job_id, stu_id,STATUS_WAITING)
    return handler.UPDATE(query, param)