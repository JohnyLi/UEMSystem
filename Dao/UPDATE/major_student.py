# coding=utf-8
# table: 'major_student' 的更新类

from util.DBLink import easy_connect

def INSERT_NEW_major_student(major_id,stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "insert into major_student values (%s,%s)"
    param = (int(stu_id),int(major_id))
    result = handler.UPDATE(query, param)
    return result

def UPDATE_major_student(major_id,stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "update major_student set major_id = %s where stu_id = %s"
    param = (int(major_id),int(stu_id))
    result = handler.UPDATE(query, param)
    return result

def DELETE_major_student(stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "delete from major_student where stu_id = %s"
    param = (stu_id)
    result = handler.UPDATE(query, param)
    return result

