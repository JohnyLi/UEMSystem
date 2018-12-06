

from startService import getSQLHandler 

def api_loginImpl():
    """
    :INPUT: {'user_name':<user_name> -> str ,'password':<password> -> str}
    :return: {'status': 'success'} or {'status': 'fail'}
    """
    handler = getSQLHandler()   # 获取sql连接



    return "1"