# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from executor.models import Executor
from django.conf.locale.en import formats as en_formats
from django.contrib import admin
en_formats.DATETIME_FORMAT = "d-m-Y H:i:s"

# Register your models here.
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('interval', 'running', 'timestamp')

# Register your models here.
admin.site.register(Executor, ExecutorAdmin)