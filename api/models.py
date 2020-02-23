# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.fullname)

class Blog(models.Model):
    title = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    content = models.TextField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s: %s' % (self.title, self.place)
