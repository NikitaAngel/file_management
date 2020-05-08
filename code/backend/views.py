from rest_framework.viewsets import ModelViewSet
# from .models import UploadFile
# from .serializers import UploadFileSerializer
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import action
import os
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
import json
from django.core.mail import send_mail
from django.core.mail import EmailMessage



class UploadFileList(generics.ListCreateAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer


class UploadFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UploadFile.objects.all()
    serializer_class = UploadFileSerializer

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = UploadFile.objects.get(pk=pk)
        ser = UploadFileSerializer(instance=queryset, many=False)
        return Response(ser.data)

    # def get_file(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     file_dir = 'file_manegement/file'
    #     file_path = os.path.join(file_dir, str(
    #         UploadFile.objects.get(pk=pk).file))
    #     return file_path


    def patch(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        queryset = UploadFile.objects.get(pk=id)
        file_dir = 'file_manegement/file'
        file_path = os.path.join(file_dir, str(
            UploadFile.objects.get(pk=id).file))
        data = request.data
        Subject = data.get('subject')
        Content = data.get('content')
        Email = data.get('mail')
        email = EmailMessage(
            subject=Subject,
            body=Content,
            from_email=settings.EMAIL_HOST_USER,  
            to=Email, 
        )
        email.attach_file(file_path, mimetype=None)
        email.send()
        return Response('Please note that the test email has been sent')
