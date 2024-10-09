from django.urls import path
from .views import DiaryListCreateView, DiaryDetailView, DiaryDeleteView

urlpatterns = [
    path('diaries/', DiaryListCreateView.as_view(), name='diary-list-create'),  # สำหรับ GET, POST
    path('diaries/<int:pk>/', DiaryDetailView.as_view(), name='diary-detail'),  # สำหรับ GET, PUT, DELETE
    path('diaries/', DiaryDetailView.as_view(), name='diary-detail'),
    path('diaries/<int:pk>/', DiaryDeleteView.as_view(), name='diary-delete'),  # Add this line


]
