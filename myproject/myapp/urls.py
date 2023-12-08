from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.file_upload, name='file_upload'),
    path('files/', views.list_files, name='list_files'),
]
