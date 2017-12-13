from django.contrib import admin
from admin_ass import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.RoleInfo)
admin.site.register(models.BossInfo)
admin.site.register(models.SummonInfo)
