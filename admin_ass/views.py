from django.shortcuts import render, HttpResponse
from admin_ass import models
import json


# Create your views here.

def login_admin(request):
    return render(request, 'login_admin.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def user_create(request):
    return HttpResponse('create success')
