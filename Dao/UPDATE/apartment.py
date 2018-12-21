# coding=utf-8
# table: 'student' 的更新类

from util.DBLink import easy_connect
from conf.Config import *

def ADD_NEW_apartment(apart_name,handler=None):
    if not handler:
        handler = easy_connect()
    query = "insert into apartment (apart_name) values(%s)"
    param = (apart_name)
    return handler.UPDATE(query, param)