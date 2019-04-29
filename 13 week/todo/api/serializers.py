from rest_framework import serializers
from api.models import TaskList,Task
from django.contrib.auth.models import User

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = TaskList(**validated_data)
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    class Meta:
        model= User
        fields = ('id', 'username', 'email')

class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by= UserSerializer(read_only=True)
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by')

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.CharField()
    due_on = serializers.CharField()
    status = serializers.CharField()
    task_list = TaskListSerializer2()


