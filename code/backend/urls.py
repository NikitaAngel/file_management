from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('file_management/', views.UploadFileList.as_view()),
    path('file_management/<int:pk>/', views.UploadFileDetail.as_view()),
    # path('file_management/', views.SendEmailList.as_view()),
    # path('file_management/<int:pk>/', views.SendEmailDetail.as_view()),
]
