# coding=utf-8

##### URL配置
##### =================================

##### WEB ====
WEB_welcome = "/"  # 欢迎界面
WEB_login = "/login"  # 登录界面
WEB_look = "/look"  # 查询界面
WEB_student_info="/student/info" #学生信息界面
WEB_student_employ_con = "/student/register" # 登记就业情况

WEB_admin_info = "/admin/info" # 管理员信息界面
WEB_change_password="/change/password"  # 密码修改界面
WEB_register_con="/student/register/con" #登记审核查询界面
WEB_student_management="/admin/student/management" #管理员学生管理界面
WEB_major_management="/admin/major/management" #管理员专业管理界面
WEB_company_management="/admin/company/managent" #管理员公司管理界面
WEB_admin_employ_con="/admin/student/register" #管理员学生登记界面
WEB_register_check="/admin/register/check" #管理员登记审核界面


##### API ====
API_login = "/api/login"  # 登录
API_getAllAccountInfo = "/api/getAllAccountInfo"  # 获取所有用户的信息
API_change_password="/api/change/password" # 修改密码
API_register="/api/register"  #就业登记
API_student_management="/api/student/management" #学生管理
API_major_management="/api/major/management" #专业管理


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


STUDENT_BAR = [("查询往年就业情况",WEB_look),('个人信息',WEB_student_info),('就业登记',WEB_student_employ_con),
               ('审核状态',WEB_register_con)]

ADMIN_BAR = [("查询往年就业情况",WEB_look),('个人信息',WEB_admin_info),
             ("学生管理",WEB_student_management),("专业管理",WEB_major_management),
             ("公司招聘信息",WEB_company_management),
             ("就业登记", WEB_admin_employ_con),("登记审核",WEB_register_check),
             ]



