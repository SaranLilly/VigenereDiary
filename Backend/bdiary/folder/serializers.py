from rest_framework import serializers
from .models import Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'  # หรือระบุฟิลด์ที่ต้องการเฉพาะ
