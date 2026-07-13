from django.db import models

# Model to store uploaded images
class ImageUpload(models.Model):
    # Storing the URL of the image from ImageKit instead of the file itself
    image_url = models.URLField(max_length=500)
    # Storing the file ID from ImageKit for management purposes
    image_file_id = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"

# Model to store polygon data for each image
class Annotation(models.Model):
    # Foreign key links the annotation to a specific image [cite: 43]
    image = models.ForeignKey(ImageUpload, related_name='annotations', on_delete=models.CASCADE)
    
    # Storing polygon coordinates as a JSON object (flexible for different shapes) [cite: 40]
    shape_data = models.JSONField() 
    
    # To keep track of what kind of shape or label it is
    label = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Annotation on Image {self.image.id}"