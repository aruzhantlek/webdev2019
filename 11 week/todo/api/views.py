from django.shortcuts import render
from django.http import JsonResponse
from django.db import models
from api.models import Task, TaskList
from datetime import datetime
def task_lists(request):
    task_list = TaskList.objects.all()
    json_tasks = [t.to_json() for t in task_list]
    return JsonResponse(json_tasks, safe=False)


def task_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json())

def tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    json_task = [t.to_json() for t in tasks]
    return JsonResponse(json_task, safe=False)
