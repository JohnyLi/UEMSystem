# coding=utf-8
# table: 'student_job' 的更新类

from util.DBLink import easy_connect
from util.Time import *
def INSERT_NEW_student_job(stu_id,com_job_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "insert into student_job values (%s,%s,%s)"
    param = (stu_id,com_job_id,from_year_to_second())
    result = handler.UPDATE(query, param)
    return result


def DELETE_student_job(stu_id,com_job_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "delete from student_job where stu_id=%s and com_job_id=%s"
    param = (stu_id,com_job_id)
    result = handler.UPDATE(query, param)
    return result

def DELETE_student_IN_student_job(stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "delete from student_job where stu_id=%s"
    param = (stu_id)
    result = handler.UPDATE(query, param)
    return result