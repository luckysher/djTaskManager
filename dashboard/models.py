# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)

    def __unicode__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('Done', 'Done'),
        ('In Progress', 'In Progress'),
        ('Not done', 'Not done'),
    )

    tid = models.AutoField(primary_key=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=250, default=None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    datetime = models.DateField()

    def __unicode__(self):
        return "%s( %s.....)" % (self.name, self.task[:30])