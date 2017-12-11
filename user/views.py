from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def login(request):
    # request 包含用户提交的所有信息
    # get 获取数据  post 提交数据
    error_msg = ""
    if request.method == "POST":
        # 获取用户用POST提交过来的数据
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email == '13547399@qq.com' and password == 'wj850820':
            # 跳转到别的地方去
            return redirect('/home/')
        else:
            # 用户名密码不匹配
            error_msg = "用户名或密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = []


def home(request):
    if request.method == "POST":
        # u = request.POST.get('username', None)
        # e = request.POST.get('email', None)
        # g = request.POST.get('gender', None)
        # temp = {'username': u, 'email': e, 'gender': g}
        # USER_LIST.append(temp)
        # favor = request.POST.getlist('favor', None)
        # for i in favor:
        #     USER_LIST.append(i)
        #     print(i,type(i))
        import os

        file = request.FILES.get('user_file')
        file_path = os.path.join('upload', file.name)
        with open(file_path, mode='wb') as f:
            for i in file.chunks():
                f.write(i)

    return render(request, 'home.html')  # , {'user_list': USER_LIST})
