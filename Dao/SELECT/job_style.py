# coding=utf-8
# table: 'job_style' 的查询类
from util.DBLink import easy_connect


def CHECK_style_name_exist(style_name, handler=None):
    if not handler:
        handler = easy_connect()
    query = "select * from job_style where style_name = %s"
    param = (style_name)
    result = handler.SELECT(query, param)
    if len(result) == 0:
        return False
    else:
        return True


def GET_ALL_style_infos(handler=None):
    if not handler:
        handler = easy_connect()
    query = "select * from job_style"
    return handler.SELECT(query)