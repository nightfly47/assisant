from django.db import models


# Create your models here.

class UserInfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=64, null=True)
    status = models.BooleanField(default=False)
    user_create = models.DateTimeField(auto_now_add=True, null=True)
    time_limit = models.DateTimeField(auto_now=True, null=True)
    user_config = models.TextField(null=True)


class RoleInfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()


class BossInfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()


class SummonInfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=32, unique=True)
    skills = models.TextField()
