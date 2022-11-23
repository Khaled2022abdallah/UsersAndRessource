from django.db import models
from datetime import datetime

from rest_framework.authtoken.admin import User


# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    avatar = models.URLField()
    job = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    urlSupport = models.URLField()
    textSupport = models.TextField()
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
        }

    def serialize2(self):
        return {
            "url": self.urlSupport,
            "text": self.textSupport,
        }

    def serializePOST(self):
        return {
            "name": self.first_name,
            "job": self.job,
            "id": self.id,
            "createdAt": self.date_created,
        }

    def serializePUT(self):
        return {
            "name": self.first_name,
            "job": self.job,
            "createdAt": self.date_created,
        }


class Resource(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    pantone_value = models.CharField(max_length=100)
    urlSupport = models.URLField()
    textSupport = models.TextField()
    user_id = models.IntegerField(blank=True, null=True,default='1')

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "color": self.color,
            "pantone_value": self.pantone_value,
        }

    def serialize2(self):
        return {
            "url": self.urlSupport,
            "text": self.textSupport,
        }


class UserToken(models.Model):
    """Responsible for storing user tokens"""
    user = models.ForeignKey(User, models.CASCADE)  # user
    token = models.UUIDField()  # token that the user will pass in request
