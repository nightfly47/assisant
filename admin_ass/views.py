from django.shortcuts import render


# Create your views here.

def login_admin(request):
    return render(request, 'login_admin.html')


def admin_home(request):
    return render(request, 'admin_home.html')
