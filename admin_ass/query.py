from django.shortcuts import render, HttpResponse
from admin_ass import models
import json


# 数据查询和添加

def query(request, db):
    db_dict = {'name': '', 'skills': {}}
    if request.method == "GET":
        data = request.GET.get('name')
        if db.objects.filter(name=data).first():
            db_data = db.objects.filter(name=data).first()
            db_dict['name'] = db_data.name
            db_dict['skills'] = db_data.skills
            data_json = json.dumps(db_dict)
            print(data_json)
            return HttpResponse(data_json, content_type='application/json')
        else:
            return HttpResponse("failed")
    elif request.method == "POST":
        json_data = request.body
        data = json.loads(json_data)
        name = data['name']
        skills = data['skills']
        if db.objects.filter(name=name).first() is None:
            print(name, skills)
            db.objects.create(name=name, skills=skills)
            return HttpResponse('ok')
        elif db.objects.filter(name=name).first():
            db.objects.filter(name=name).update(skills=skills)
            return HttpResponse('ok')
        else:
            return HttpResponse('failed')
    else:
        return HttpResponse('failed')


def role_query(request, db=models.RoleInfo):
    return query(request, db)


# boss 数据库操作
def boss_query(request, db=models.BossInfo):
    return query(request, db)


# summon 数据库操作
def summon_query(request, db=models.SummonInfo):
    return query(request, db)


# 查询和更新用户配置
def config_query(request, db):
    db_dict = {'name': '', 'usr_config': {}}
    if request.method == "GET":
        data = request.GET.get('name')
        if db.objects.filter(name=data).first():
            db_data = db.objects.filter(name=data).first()
            db_dict['name'] = db_data.name
            db_dict['usr_config'] = db_data.user_config
            data_json = json.dumps(db_dict)
            return HttpResponse(data_json, content_type='application/json')
        else:
            return HttpResponse("failed")
    elif request.method == "POST":
        json_data = request.body
        data = json.loads(json_data)
        name = data['name']
        user_config = data['user_config']
        if db.objects.filter(name=name).first() is None:
            return HttpResponse('failed,user not exist')
        elif db.objects.filter(name=name).first():
            db.objects.filter(name=name).update(user_config=user_config)
            return HttpResponse('ok')
        else:
            return HttpResponse('failed')
    else:
        return HttpResponse('failed')
