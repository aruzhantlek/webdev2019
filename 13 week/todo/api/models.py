from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TaskListManager(models.Manager):
    def for_user_order_by_name(self, user):
        self.filter(created_by= user).order_by('name')



class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = TaskListManager()
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    due_on = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return 'Task list: {}\n{}: {}\nStatus: {}'.format(self.task_list.name, self.id, self.name, self.status)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'task_list': self.task_list.name
        }
