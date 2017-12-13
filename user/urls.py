from django.urls import path
from user import views


urlpatterns = [
    path('login/', views.login),
    path('home', views.home),
]