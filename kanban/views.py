from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    # This viewset automatically provides list, create, retrieve, update, and destroy actions
    queryset = Task.objects.all()
    serializer_class = TaskSerializer