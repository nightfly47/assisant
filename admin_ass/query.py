from django.shortcuts import HttpResponse
from admin_ass import models
from django.db import utils
import json


# 数据查询和添加

def query(request, db):
    db_dict = {}
    data_dict = {}
    if request.method == "GET":
        get_data = request.GET.getlist('data')  # 获取data里面所有的值
        for id_get in get_data:
            db_data = db.objects.filter(uid=id_get).first()
            if db_data is None:
                pass  # 没有找到就跳出当次循环，接着找下一条
            else:
                data_dict['uid'] = db_data.name
        skill_json = json.dumps(data_dict)
        return HttpResponse(skill_json, content_type='application/json')
    elif request.method == "POST":
        json_data = request.body
        dict_data = json.loads(json_data)
        for key, data in dict_data.items():
            if db.objects.filter(name=data['name'], uid=data['id']) \
                    .update(name=data['name'], uid=data['id']):
                db_dict[key] = 'update success'
            else:
                try:
                    db.objects.create(
                        name=data['name'],
                        uid=data['id']
                    )
                except utils.IntegrityError:
                    db_dict[key] = 'create failed'
                else:
                    db_dict[key] = 'create success'
        json_dict = json.dumps(db_dict)
        return HttpResponse(json_dict, content_type='application/json')


def role_query(request, db=models.RoleInfo):
    return query(request, db)


# boss 数据库操作
def boss_query(request, db=models.BossInfo):
    return query(request, db)


# summon 数据库操作
def summon_query(request, db=models.SummonInfo):
    return query(request, db)


# 查询,添加用户技能配置
def user_skills_config(request, db=models.UserSkillConfig):
    report_list = {}
    skill_dict = {}
    if request.method == 'GET':
        get_id = request.GET.get('user_id')
        get_roles = request.GET.getlist('data')  # 获取data里面所有的值
        for role_id_get in get_roles:
            db_role = db.objects.filter(user_id_id=get_id, role_id_id=role_id_get).first()
            if db_role is None:
                pass  # 没有找到就跳出当次循环，接着找下一条
            else:
                skill_dict[role_id_get] = db_role.skill_config
        skill_json = json.dumps(skill_dict)
        return HttpResponse(skill_json, content_type='application/json')
    elif request.method == 'POST':
        json_data = request.body
        data = json.loads(json_data)
        for key, role in data.items():
            user_id = role['user_id']
            role_id = role['role_id']
            skill_config = role['skill_config']
            if db.objects.filter(user_id_id=user_id, role_id_id=role_id).update(skill_config=skill_config):
                report_list[key] = 'update success'
            else:
                try:
                    db.objects.create(
                        user_id_id=user_id,
                        role_id_id=role_id,
                        skill_config=skill_config)
                except utils.IntegrityError:
                    report_list[key] = 'create failed'
                else:
                    report_list[key] = 'create success'
        json_report = json.dumps(report_list)
        return HttpResponse(json_report, content_type='application/json')
    else:
        return HttpResponse('failed')
