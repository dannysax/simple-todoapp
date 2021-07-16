from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task


api_view(["GET"])
def url_overview(request):
    url_list = [{
        "task-list": "task/task-list",
        "task-create": "task/create",
        "task-update": "task/update/<id>",
        "task-delete": "task/delete/<id>"
    }]
    
    return JsonResponse(url_list, safe=False)

@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(data = serializer.data)

@api_view(["POST"])
def task_create(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def task_edit(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task deleted') 