# coding=utf-8
# table: 'major' 的查询类

from util.DBLink import easy_connect
def GET_ALL_major(handler=easy_connect):
    if not handler:
        handler=easy_connect()
    query = "select major_name from major"
    param = ()
    result = handler.SELECT(query,param)
    if len(result)==0:
        return []
    else:
        new_result = []
        for row in result:
            new_result.append(row[0])
        return new_result

def GET_major_name_BY_major_id(major_id,handler=easy_connect()):
    if not handler:
        handler=easy_connect()
    query = "select major_name from major where major_id=%s"
    param = (major_id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0][0]