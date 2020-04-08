from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def get_file_dir():
    file_dir = 'file_management/files/'
    return file_dir


class UploadFile(models.Model):
    upload_file_dir = get_file_dir()
    file = models.FileField(upload_to=upload_file_dir)

    user = models.ForeignKey(User, on_delete=models.CASCADE)    # Every server monitor refers to a user
    file_name = models.CharField(max_length=30, default='', unique=True)
    # Information needed to login the server
    date = models.CharField(max_length=30, default='')
    upload_date = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField()      # Target email address when warning email was sent

    def __str__(self):
        return self.file_name

'''
class IDMap(models.Model):
    encrypted_id = models.CharField(max_length=200, unique=True)
    internal_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.internal_id


# [Note] This model can only have one object, multiple objects will cause error
class SerialNumber(models.Model):
    serial_number = models.IntegerField(default=0)

    def to_string(self):
        s = str(self.serial_number)
        assert(len(s) <= 7), "Serial number overflow!"
        return s.zfill(7)
'''

