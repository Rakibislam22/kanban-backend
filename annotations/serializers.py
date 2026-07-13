from rest_framework import serializers
from .models import ImageUpload, Annotation

class ImageUploadSerializer(serializers.ModelSerializer):
    # Define the field once with all necessary arguments
    image = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = ImageUpload
        fields = ['id', 'image_url', 'image_file_id', 'uploaded_at', 'image']
        read_only_fields = ['id', 'image_url', 'image_file_id', 'uploaded_at']

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = '__all__'