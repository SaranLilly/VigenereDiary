# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}  # Prevent password from being exposed in the response
#         }

#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])  # Hash the password
#         user.save()
#         return user


from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Prevent password from being exposed in the response
        }

    # def create(self, validated_data):
    #     # ใช้ UserManager เพื่อสร้างผู้ใช้
    #     user = User.objects.create_user(**validated_data)
    #     return user



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name',
#                   'password', 'date_of_birth', 'gender', 'profile_picture']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
