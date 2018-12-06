from flask import session
from startService import getSQLHandler
from Dao import *
def check_session():
    handler = getSQLHandler()
    if (not session.get('user_name')) or (not session.get('privilege')):
        return False
    else:
        user_name = session['user_name']
        if CHECK_USER_IS_EXIST(handler,user_name):
            return True
        else:
            return False