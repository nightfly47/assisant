from django.urls import path
from admin_ass import views

urlpatterns = [
    path('login_admin/', views.login_admin),
    path('admin_home/', views.admin_home),
    path('get_roles/', views.get_roles),
    path('post_role/', views.post_role),
]
