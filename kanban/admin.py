from django.contrib import admin
from .models import Task

# Registering the Task model so it appears in the admin panel
admin.site.register(Task)