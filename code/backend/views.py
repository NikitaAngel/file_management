from rest_framework.viewsets import ModelViewSet
from .models import UploadFile
from .serializers import UploadFileSerializer
from rest_framework import generics

class UploadFileList(generics.ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer

class UploadFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer
