from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


class Tasklist(APIView):
    def get(self, request):
        task_lists= TaskList.objects.all()
        serializer= TaskListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer= TaskListSerializer2(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class Tasklist_detail(APIView):
    def get_objects(self, pk):
        try:
            return TaskList.objects.get(id= pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_lists= self.get_objects(pk)
        serializer= TaskListSerializer2(task_lists)
        return Response(serializer.data)
    def put(self, request, pk):
        task_lists =self.get_objects(pk)
        serializer= TaskListSerializer2(instance=task_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, pk):
        task_lists= self.get_objects(pk)
        task_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ListTask(APIView):
    def get_objects(self, pk):
        try:
            return TaskList.objects.get(id= pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tasks= self.get_objects(pk)
        serializer= TaskSerializer(tasks, many=True)
        return Response(serializer.data)

