# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from security.models import TaskUser


class Task(models.Model):
    STATUS_CHOICES = (
        (0, 'Not done'),
        (1, 'In Progress'),
        (2, 'Done'),)

    tid = models.AutoField(verbose_name="Task Id",
                           primary_key=True)
    user_id = models.ForeignKey(TaskUser)
    taskname = models.CharField(verbose_name="Short name for task",
                                max_length=30)
    task = models.CharField(verbose_name="Task with details",
                            max_length=250,
                            blank=False)
    status = models.IntegerField(verbose_name="Status of task",
                                 choices=STATUS_CHOICES,
                                 default=0)
    duedate = models.DateField(verbose_name='Dau date for task',
                               blank=False)
    time = models.TimeField(verbose_name='Time',
                            blank=False)

    def __unicode__(self):
        return "%s( %s.....)" % (self.taskname, self.task[:30])