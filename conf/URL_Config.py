# coding=utf-8

##### URL配置
##### =================================

##### WEB ====
WEB_welcome = "/"  # 欢迎界面
WEB_login = "/login"  # 登录界面






##### API ====
API_getAllAccountInfo = "/api/getAllAccountInfo"  # 获取所有用户的信息





##### 制作URL的字典
##### =================================
url_local = locals().copy()
url_dict = {} # 所有URL的字典
for key in url_local.keys():
    if "__" not in key:
        url_dict[key]=url_local[key]
del url_local,key

