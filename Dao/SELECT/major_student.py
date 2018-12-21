# coding=utf-8
# table: 'major_student' 的查询类

from util.DBLink import easy_connect
def GET_major_id_BY_stu_id(stu_id,handler=None):
    """
    通过学生id获取专业id
    :param stu_id: int
    :param handler: SQLHandler
    :return:
    """
    if not handler:
        handler=easy_connect()
    query = "select major_id from major_student where stu_id=%s"
    param = (stu_id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0][0]

def GET_ALL_major_student_INFOS(handler=None):
    """

    :param handler:
    :return:
    """
    if not handler:
        handler=easy_connect()
    query = "select * from major_student"
    param = ()
    result = handler.SELECT(query,param)
    return result


def GET_major_name_BY_stu_id(stu_id,handler=None):
    """
        通过学生id获取专业名
        :param stu_id: int
        :param handler: SQLHandler
        :return:
        """
    if not handler:
        handler = easy_connect()
    query = "select major_name from v_major_student_infos where stu_id = %s"
    param = (stu_id)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return None
    else:
        return result[0][0]


def GET_ALL_STUDENT_INFOS(handler=None):
    if not handler:
        handler = easy_connect()
    query = "select * from v_major_student_infos"
    param = ()
    result = handler.SELECT(query, param)
    return result





