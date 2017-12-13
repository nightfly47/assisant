from django.shortcuts import render, HttpResponse
from admin_ass import models
import json


# Create your views here.

def login_admin(request):
    return render(request, 'login_admin.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def get_roles(request):
    role_list = []
    if request.mothod == "GET":
        roles = models.RoleInfo.objects.all()
        for role in roles:
            role_dict = role.skills
            role_list.append(role_dict)

    role_json = json.dumps(role_list)
    return HttpResponse(role_json, content_type='application/json')


def post_role(request):
    if request.method == "POST":
        json_data = request.body
        print(json_data)
        data = json.loads(json_data)
        print(request)
        print(json)
        print(data)
        name = data['name']
        skills = data['skills']
        print(name, skills)
        models.RoleInfo.objects.create(name=name, skills=skills)
        return HttpResponse('ok')
    elif request.method == "GET":
        return HttpResponse('failed,post please')
    else:
        return HttpResponse('failed,post please')
