# coding=utf-8
# table: 'student_job' 的查询类

from util.DBLink import easy_connect

def CHECK_student_pass_or_not(stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "select * from student_job where stu_id = %s"
    param = (stu_id)
    result = handler.SELECT(query, param)
    if len(result)==0:
        return False
    else:
        return True

def GET_student_job_info_BY_stu_id(stu_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "select * from v_student_job_info where stu_id = %s"
    param = (stu_id)
    result = handler.SELECT(query, param)
    if len(result)==0:
        return None
    else:
        return result[0]

