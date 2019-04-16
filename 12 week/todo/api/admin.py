from django.contrib import admin
from api.models import Task, TaskList

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskList)