from flask import session,g
from Dao.SELECT.admin import CHECK_USER_IS_EXIST
from util.DBLink import *
def getSQLHandler():
    """
    :return: SQLHandler
    """
    if not hasattr(g, 'handler'):
        sqlServer = g.sqlServer
        conn = sqlServer.getConn()
        g.handler = SQLHandler(conn)

    return g.handler

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

