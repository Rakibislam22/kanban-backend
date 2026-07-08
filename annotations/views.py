from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import ImageUpload, Annotation
from .serializers import ImageUploadSerializer, AnnotationSerializer

class ImageUploadViewSet(viewsets.ModelViewSet):
    # Handles image uploads to the backend [cite: 34]
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

class AnnotationViewSet(viewsets.ModelViewSet):
    # Saves drawn shapes into the database [cite: 37]
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer