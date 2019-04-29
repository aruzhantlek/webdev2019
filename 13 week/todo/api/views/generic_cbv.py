from django.contrib.auth.models import User
from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class Tasklist(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2

class Lists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
