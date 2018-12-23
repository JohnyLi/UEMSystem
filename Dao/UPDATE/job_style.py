# coding=utf-8
# table: 'job_style' 的更新类
from util.DBLink import easy_connect
def NEW_job_style(style_name,handler=None):
    if not handler:
        handler=easy_connect()
    query = "insert into job_style (style_name) values (%s)"
    param = (style_name)
    return handler.UPDATE(query, param)