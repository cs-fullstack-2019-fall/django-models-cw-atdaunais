from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


class Account(models.Model):
    username = models.CharField(max_length=15)
    realName = models.CharField(max_length=50)
    accountNumber = models.IntegerField()
    balance = models.IntegerField()


