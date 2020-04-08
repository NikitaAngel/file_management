from django.conf.urls import url, include
from backend import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('uploadfile/', views.UploadFileList.as_view()),
    path('uploadfile/<int:pk>/', views.UploadFileDetail.as_view()),
]
