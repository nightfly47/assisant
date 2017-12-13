from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=64, null=True)
    status = models.BooleanField(default=False)
    user_create = models.DateTimeField(auto_now_add=True, null=True)
    time_limit = models.DateTimeField(auto_now=True, null=True)
    user_config = models.TextField()


class RoleInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()


class BossInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()


class SummonInfo(models.Model):
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()
