from django.urls import path
from admin_ass import views
from admin_ass import query

urlpatterns = [
    path('login_admin/', views.login_admin),
    path('admin_home/', views.admin_home),
    path('role/', query.role_query),
    path('summon/', query.summon_query),
    path('boss/', query.boss_query),
    path('config/', query.user_skills_config),
]
