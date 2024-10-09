from django.urls import path
from .views import FolderListCreateView, FolderDetailView

urlpatterns = [
    path('folders/', FolderListCreateView.as_view(), name='folder-list-create'),  # สำหรับ GET, POST
    path('folders/<int:pk>/', FolderDetailView.as_view(), name='folder-detail'),  # สำหรับ GET, PUT, DELETE
    
    
]
