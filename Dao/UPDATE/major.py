# coding=utf-8
# table: 'major' 的更新类

from util.DBLink import easy_connect
def ADD_NEW_major(major_name,handler=None):
    if not handler:
        handler = easy_connect()
    query = "insert into major (major_name) values(%s)"
    param = (major_name)
    return handler.UPDATE(query, param)