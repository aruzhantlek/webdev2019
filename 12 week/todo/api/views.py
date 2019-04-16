import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Task, TaskList
from api.serializers import ListSerializer, ListSerializer2, TaskSerializer


@csrf_exempt
def task_lists(request):
    if request.method=='GET':
      all_lists = TaskList.objects.all()
      serializer=ListSerializer(all_lists, many=True)
      return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data=json.loads(request.body)
        serializer=ListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors)
    return JsonResponse({'errror':'bad request'})


@csrf_exempt
def task_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer=ListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data=json.loads(request.body)
        serializer=ListSerializer(instance=task_list,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=204)

@csrf_exempt
def tasks(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        tasks = list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data=json.loads(request.body)
        print(data)
        TaskSerializer.listik=list
        serializer=TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors)


