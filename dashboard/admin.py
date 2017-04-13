# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from security.models import TaskUser

# Register your models here.

admin.site.register(TaskUser)
admin.site.register(Task)