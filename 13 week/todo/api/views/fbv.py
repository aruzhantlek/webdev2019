from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()  # It will use create function in serializer class beacuse it is POST request
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR )

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        tasklist_item= TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer2(tasklist_item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer2(instance=tasklist_item, data=request.data)
        if serializer.is_valid():
            serializer.save() #It will use update function in serializer class, because it is PUT request
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        tasklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tasks(request, pk):
    try:
        tasklist_item = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        tasks = tasklist_item.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

