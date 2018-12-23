# coding=utf-8
# table: 'student' 的查询类

from util.DBLink import easy_connect
from conf.Config import *
from util.Sha import get_sha
def GET_ALL_student_INFO_BY_YEAR(year,handler=None):
    """
    获取
    :param year:
    :param handler:
    :return:
    """
    if not handler:
        handler=easy_connect()
    query = "select * from student where gradu_year=%s"
    param = (year)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return []
    else:
        return result


def GET_ALL_gradu_Year(handler=None):
    if not handler:
        handler=easy_connect()
    query = "select DISTINCT gradu_year from student "
    param = ()
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return []
    else:
        new_result = []
        for row in result:
            new_result.append(row[0])
        return new_result

def GET_student_INFO_BY_ID(id,handler=None):

    if not handler:
        handler=easy_connect()
    query = "select * from student where stu_id=%s"
    param = (id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0]

def GET_student_major_INFO_BY_ID(id, handler=None):

    if not handler:
        handler = easy_connect()
    query = "select * from v_major_student_infos where stu_id=%s"
    param = (id)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return None
    else:
        return result[0]

def CHECK_stu_id_AND_password(stu_id,password,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select password from student where stu_id=%s"
    param = (stu_id)
    result = handler.SELECT(query, param)
    if len(result)==0:
        return False
    real_password = result[0][0]
    if real_password == None:
        if password == Default_password:
            return True
        else:
            return False
    else:
        if get_sha(password)==real_password:
            return True
        else:
            return False




