
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('vigenere-diary/', include('users.urls')),
    path('vigenere-diary/', include('diary.urls')),
    path('vigenere-diary/', include('folder.urls')),
    path('vigenere-diary/', include('users.urls')),
]
