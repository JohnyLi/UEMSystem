# coding=utf-8

##### URL配置
##### =================================

##### WEB ====
WEB_welcome = "/"  # 欢迎界面
WEB_login = "/login"  # 登录界面
WEB_look = "/look"  # 查询界面
WEB_student_info="/student/info" #学生信息界面
WEB_student_employ_con = "/student/employ_con" # 登记就业情况

WEB_admin_info = "/admin/info" # 管理员信息界面


##### API ====
API_login = "/api/login"  # 登录
API_getAllAccountInfo = "/api/getAllAccountInfo"  # 获取所有用户的信息


##### LOGOUT ====
URL_LOGOUT = "/logout"


##### 制作URL的字典
##### =================================
url_local = locals().copy()
url_dict = {} # 所有URL的字典
for key in url_local.keys():
    if "__" not in key:
        url_dict[key]=url_local[key]
del url_local,key


STUDENT_BAR = [("查询往年就业情况",WEB_look+"1"),('个人信息',WEB_student_info),('就业登记',WEB_student_employ_con)]



