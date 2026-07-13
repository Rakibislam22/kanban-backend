from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
import traceback
import requests  # Using requests directly to bypass a known bug in imagekitio SDK v4.x

from .models import ImageUpload, Annotation
from .serializers import ImageUploadSerializer, AnnotationSerializer
from .imagekit_utils import imagekit  # Still used for the auth endpoint below


# ImageKit's official REST upload endpoint (bypasses the buggy SDK upload method)
IMAGEKIT_UPLOAD_URL = "https://upload.imagekit.io/api/v1/files/upload"


def upload_to_imagekit(binary_data: bytes, file_name: str) -> dict:
    """
    Uploads raw binary data to ImageKit using a direct REST call instead of
    the imagekitio SDK's upload_file() method.

    WHY: In imagekitio SDK v4.x, when you pass raw bytes/str to upload_file(),
    the SDK builds the multipart file part WITHOUT a "filename" attribute
    (see file.py -> isinstance(file, str) or isinstance(file, bytes) branch).
    Without a filename, ImageKit's server does not treat the part as true
    binary file data, which corrupts the upload (tiny broken files).

    Calling requests.post() ourselves lets us set the filename correctly via
    the tuple (file_name, binary_data, content_type), which fixes the issue.
    """
    # ImageKit uses HTTP Basic Auth with the private key as username, empty password
    auth = (settings.IMAGEKIT_PRIVATE_KEY, "")

    # The tuple format (filename, file_bytes, content_type) ensures the
    # multipart part includes a proper filename, unlike the broken SDK path
    files = {
        "file": (file_name, binary_data, "application/octet-stream"),
    }

    data = {
        "fileName": file_name,
        "useUniqueFileName": "true",
    }

    response = requests.post(IMAGEKIT_UPLOAD_URL, files=files, data=data, auth=auth)
    response.raise_for_status()  # Raises an exception for 4xx/5xx responses
    return response.json()


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer

    def create(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No file'}, status=400)

        # Force move to start
        image_file.seek(0)
        # Read full data
        binary_data = image_file.read()

        print(f"DEBUG: Final binary size: {len(binary_data)} bytes")

        if len(binary_data) < 100:  # Image size should never be under 100 bytes
            return Response({'error': 'File corrupted: Size too small'}, status=400)

        try:
            # Direct REST call instead of imagekit.upload_file() to avoid the SDK bug
            upload_response = upload_to_imagekit(binary_data, image_file.name)

            instance = ImageUpload.objects.create(
                image_url=upload_response["url"],
                image_file_id=upload_response["fileId"]
            )
            return Response(self.get_serializer(instance).data, status=201)

        except requests.exceptions.HTTPError as e:
            # Log the actual ImageKit error response body for debugging
            print("DEBUG: ImageKit error response:", e.response.text if e.response else str(e))
            traceback.print_exc()
            return Response({'error': str(e)}, status=500)

        except Exception as e:
            traceback.print_exc()
            return Response({'error': str(e)}, status=500)


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['image']


class ImageKitAuthView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        try:
            auth_params = imagekit.get_authentication_parameters()
            return Response(auth_params, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        