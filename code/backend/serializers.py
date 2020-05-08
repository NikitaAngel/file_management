from rest_framework import serializers
from .models import UploadFile

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = (
            'id', 'mail', 'file', 'subject', 'content'
        )


# class SendEmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SendEmail
#         fields = (
#             'id','mail''subject','content'
#         )
