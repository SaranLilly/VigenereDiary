from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
    


class BlacklistedAccessToken(models.Model):
    token = models.CharField(max_length=500, unique=True)
    blacklisted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)  # เปลี่ยนให้ชี้ไปยังโมเดลผู้ใช้ที่กำหนดเอง

    def __str__(self):
        return self.token

    @staticmethod
    def is_blacklisted(token):
        """
        Check if the given token is blacklisted.
        """
        return BlacklistedAccessToken.objects.filter(token=token).exists()

    

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

# # class User(AbstractBaseUser):
# #     id = models.AutoField(primary_key=True)
# #     username = models.CharField(max_length=150, unique=True)
# #     # password = models.CharField(max_length=128)

   
# #     USERNAME_FIELD = 'username'
# #     REQUIRED_FIELDS = []

# #     objects = CustomUserManager()

# #     def __str__(self):
# #         return self.username
    

# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=150, unique=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_set',  # Change this line
#         blank=True,
#     )
    
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_set',  # Change this line
#         blank=True,
#     )

#     def __str__(self):
#         return self.username


# # class BlacklistedAccessToken(models.Model):
# #     token = models.CharField(max_length=500, unique=True)
# #     blacklisted_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return self.token

# class BlacklistedAccessToken(models.Model):
#     token = models.CharField(max_length=500, unique=True)
#     blacklisted_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey('users.User', on_delete=models.CASCADE, default=1)

#     def __str__(self):
#         return self.token

#     @staticmethod
#     def is_blacklisted(token):
#         """
#         Check if the given token is blacklisted.
#         """
#         return BlacklistedAccessToken.objects.filter(token=token).exists()