# Generated by Django 2.0 on 2017-12-16 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BossInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('uid', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('uid', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SummonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('uid', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_limit', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkillConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_config', models.TextField(null=True)),
                ('role_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_ass.RoleInfo', to_field='uid')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_ass.UserInfo')),
            ],
        ),
    ]
