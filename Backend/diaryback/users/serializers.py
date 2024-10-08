from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # ป้องกันไม่ให้ password ถูกแสดงออกมาทาง API response
        }
