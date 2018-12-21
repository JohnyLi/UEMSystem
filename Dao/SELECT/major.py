# coding=utf-8
# table: 'major' 的查询类

from util.DBLink import easy_connect
def GET_ALL_major(handler=None):
    """
    获取所有专业名
    :param handler: SQLHandler
    :return: list
    """
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

def GET_ALL_major_INFOS(handler=None):
    """
    获取所有专业信息,包括专业id和专业名
    :param handler: SQLHandler
    :return:
    """
    if not handler:
        handler=easy_connect()
    query = "select * from major"
    param = ()
    result = handler.SELECT(query,param)
    return result

def GET_major_name_BY_major_id(major_id,handler=None):
    """
    根据专业id获取专业名
    :param major_id: int
    :param handler: SQLHandler
    :return:
    """
    if not handler:
        handler=easy_connect()
    query = "select major_name from major where major_id=%s"
    param = (major_id)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0][0]

def GET_major_id_BY_major_name(major_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select major_id from major where major_name=%s"
    param = (major_name)
    result = handler.SELECT(query,param)
    if len(result)==0:
        return None
    else:
        return result[0][0]

def CHECK_major_name_EXIST(major_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "select * from major where major_name=%s"
    param = (major_name)
    result = handler.SELECT(query, param)
    if len(result)==0:
        return False
    else:
        return True