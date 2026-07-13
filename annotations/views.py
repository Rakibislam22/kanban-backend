from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['image']