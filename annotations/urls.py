from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadViewSet, AnnotationViewSet, ImageKitAuthView

router = DefaultRouter()
router.register(r'image-uploads', ImageUploadViewSet, basename='imageupload')
router.register(r'annotations', AnnotationViewSet, basename='annotation')

urlpatterns = [
    path('', include(router.urls)),
    path('imagekit-auth/', ImageKitAuthView.as_view(), name='imagekit-auth'),
]