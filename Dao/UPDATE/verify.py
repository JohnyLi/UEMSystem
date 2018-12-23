# coding=utf-8
# table: 'verify' 的更新类
from util.DBLink import easy_connect
from conf.Config import *
from util.Time import *

def INSERT_NEW_register(com_job_id,stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into verify (com_job_id,stu_id,status,create_time) values(%s,%s,%s,%s)"
    param = (com_job_id, stu_id,STATUS_WAITING,from_year_to_second())
    return handler.UPDATE(query, param)

def INSERT_NEW_register_AND_RETURN_verify_id(com_job_id,stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into verify (com_job_id,stu_id,status,create_time) values(%s,%s,%s,%s)"
    param = (com_job_id, stu_id,STATUS_WAITING,from_year_to_second())
    handler.UPDATE(query, param)
    query = "select max(verify_id) from verify"
    result = handler.SELECT(query)
    return result[0][0]


def UPDATE_register(verify_id,status,handler=None):
    if not handler:
        handler=easy_connect()
    query = "update verify set status=%s , treat_time = %s where verify_id=%s"
    param = (status,from_year_to_second(),verify_id)
    return handler.UPDATE(query, param)

def DELETE_student_IN_verify(verify_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "delete from verify where verify_id = %s"
    param = (verify_id)
    return handler.UPDATE(query, param)

def REFRESH_student_status(stu_id,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from verify where stu_id = %s"
    param = (stu_id)
    result = handler.SELECT(query,param)
    stu_status = "待业"
    for row in result:
        temp_status = row[3]
        if temp_status == STATUS_PASS:
            stu_status = "就业"
            break
    query = "update student set status = %s where stu_id = %s"
    param = (stu_status,stu_id)
    result = handler.UPDATE(query, param)
    return result


def DELETE_verify(verify_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "delete * from verify where verify_id = %s"
    param = (verify_id)
    result = handler.UPDATE(query, param)
    return result
