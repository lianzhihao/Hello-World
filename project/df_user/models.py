from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    userName = models.CharField(max_length=20)
    passWord = models.CharField(max_length=40)
    phoneNumber = models.CharField(max_length=20)
