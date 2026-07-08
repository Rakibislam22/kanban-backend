from django.contrib import admin
from .models import ImageUpload, Annotation

# Registering models so they appear in the Django admin panel
admin.site.register(ImageUpload)
admin.site.register(Annotation)