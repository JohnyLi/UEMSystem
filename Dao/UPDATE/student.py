# coding=utf-8
# table: 'student' 的更新类

from util.Sha import get_sha
from Dao.SELECT.admin import CHECK_USER_IS_EXIST,GET_USER_ID
from util.DBLink import easy_connect