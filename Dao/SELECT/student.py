# coding=utf-8
# table: 'student' 的查询类

from util.DBLink import easy_connect
def GET_ALL_student_INFO_BY_YEAR(year,handler=None):
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




