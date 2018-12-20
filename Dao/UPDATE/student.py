# coding=utf-8
# table: 'student' 的更新类

from util.Sha import get_sha
from util.DBLink import easy_connect
from conf.Config import *
def CHANGE_STUDENT_password(stu_id,password,handler=None):

    if not handler:
        handler=easy_connect()
    query = "update student set password=%s where stu_id=%s"
    param = ( get_sha(password), stu_id)
    return  handler.UPDATE(query, param)

def ADD_NEW_STUDENT(stu_id,stu_name,gender,enroll_year,gradu_year,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into student values(%s,%s,%s,%s,%s,%s)"
    param = (stu_id,stu_name,gender,enroll_year,gradu_year,get_sha(Default_password))
    return  handler.UPDATE(query, param)