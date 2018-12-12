# coding=utf-8
# table: 'student_major' 的查询类

from util.DBLink import easy_connect
def GET_major_id_BY_stu_id(stu_id,handler=easy_connect()):
    if not handler:
        handler=easy_connect()
    query = "select * from major_student where stu_id=%s"
    param = (stu_id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0][0]