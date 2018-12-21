# coding=utf-8
# table: 'apart_major' 的更新类

from util.DBLink import easy_connect
def ADD_NEW_apart_major(major_id,apart_id,handler=None):
    if not handler:
        handler = easy_connect()
    query = "insert into apart_major values(%s,%s)"
    param = (major_id,apart_id)
    return handler.UPDATE(query, param)