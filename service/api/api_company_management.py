from flask import jsonify,request,session
import json
from util.Functions1 import getSQLHandler,check_session
from conf.Config import *
from Dao.SELECT.com_job import *
from Dao.SELECT.company import *
from Dao.UPDATE.company import *
from Dao.UPDATE.job_style import *
from Dao.SELECT.job_style import *
from Dao.SELECT.job import *
from Dao.UPDATE.job import *
from Dao.UPDATE.com_job import *
from Dao.UPDATE.verify import *
def api_company_managementImpl():
    privilege = session['privilege']
    if privilege != PRIVILEGE_ADMIN or not check_session():
        return
    response1 = {'status': ""}
    handler = getSQLHandler()  # 获取sql连接
    data = json.loads(request.get_data().decode('utf-8'))
    control = data['control']

    if control == "get_com_job_infos":
        com_job_infos = GET_ALL_com_job_infos(handler)
        if com_job_infos != None:
            response1['data']=com_job_infos
            response1['status']="success"
        else:
            response1['status']='fail'
    elif control == "addCompany":
        com_name = data['com_name']
        if not CHECK_com_name_exist(com_name,handler):
            if NEW_company(com_name,handler):
                response1['status']="新增成功"
            else:
                response1['status']="新增失败"
        else:
            response1['status']="公司名已存在"

    elif control == "addJobStyle":
        style_name = data['style_name']
        if not CHECK_style_name_exist(style_name,handler):
            if NEW_job_style(style_name,handler):
                response1['status']="新增成功"
            else:
                response1['status']="新增失败"
        else:
            response1['status']="类型名已存在"

    elif control == "publish":
        job_name = data['job_name']
        com_id = data['com_id']
        style_id = data['style_id']
        need_num = int(data['need_num'])
        finish_date = data['end_date']

        job_id = CHECK_job_name_EXIST_AND_RETURN_job_id(job_name,handler)
        if not job_id:
            job_id = NEW_job_AND_RETURN_job_id(job_name,handler)

        if NEW_com_job(com_id,job_id,need_num,finish_date,style_id):
            response1['status']="发布成功"
        else:
            response1['status']="发布失败"

    elif control == "change":
        com_job_id = data['com_job_id']
        com_id = data['com_id']
        style_id = data['style_id']
        need_num = int(data['need_num'])
        finish_date = data['end_date']
        if UPDATE_com_job(com_job_id,com_id,need_num,finish_date,style_id):
            response1['status'] = "修改成功"
        else:
            response1['status'] = "修改失败"


    return jsonify(response1)