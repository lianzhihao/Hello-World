# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20171129_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='ConfirmPwd',
            new_name='confirmPwd',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='password',
            new_name='passWord',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='phonenumber',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='userName',
        ),
    ]