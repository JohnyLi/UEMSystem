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
    if (not session.get('user')) or (not session.get('privilege')):
        return False
    else:
        return True

def GetSideBar(sidebar, activebar=None):  # 对sidebar进行整理并返回整理好的元组
    result = []
    for row in sidebar:
        bar1 = {}
        bar1['name'] = row[0]
        bar1['href'] = row[1]
        if (activebar == row[0]):
            bar1['active'] = 'active'
        result.append(bar1)
    return result
