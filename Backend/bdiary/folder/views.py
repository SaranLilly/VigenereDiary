# # from rest_framework import generics
# # from .models import Folder
# # from .serializers import FolderSerializer
# # from rest_framework.permissions import AllowAny  # สามารถปรับให้เหมาะสมตามความต้องการ
# # from rest_framework.response import Response
# # from rest_framework import status

# # # class FolderListCreateView(generics.ListCreateAPIView):
# # #     queryset = Folder.objects.all()
# # #     serializer_class = FolderSerializer
# # #     permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ
    

# # from django.contrib.auth import get_user_model
# # from rest_framework import generics, status
# # from rest_framework.response import Response
# # from rest_framework.permissions import AllowAny
# # from .models import Folder
# # from .serializers import FolderSerializer
# # User = get_user_model()  # นำโมเดลผู้ใช้มาใช้งาน

# # class FolderListCreateView(generics.ListCreateAPIView):
# #     queryset = Folder.objects.all()
# #     serializer_class = FolderSerializer
# #     permission_classes = [AllowAny]  # ปรับแต่ง permission ตามความเหมาะสม

# #     def create(self, request, *args, **kwargs):
# #         folder_name = request.data.get('folder_name')
# #         username = request.data.get('user')  # เปลี่ยนเป็น username

# #         print(f"Received folder_name: {folder_name}, username: {username}")

# #         # ตรวจสอบว่า username ถูกส่งมาหรือไม่
# #         if not username:
# #             return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

# #         # ค้นหาผู้ใช้จาก username
# #         try:
# #             user = User.objects.get(username=username)
# #             user_id = user.id  # ดึง user_id ออกมา
# #             print(f"Found user_id: {user_id}")
# #         except User.DoesNotExist:
# #             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# #         # สร้างโฟลเดอร์พร้อมกับเชื่อมโยงกับ user_id ที่พบ
# #         folder_data = {
# #             "folder_name": folder_name,
# #             "user": user_id  # บันทึกเป็น user_id
# #         }

# #         serializer = self.get_serializer(data=folder_data)
    
# #         # ตรวจสอบความถูกต้องของ serializer
# #         if not serializer.is_valid():
# #             print(serializer.errors)  # พิมพ์ข้อผิดพลาด
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ส่งกลับข้อผิดพลาด

# #         # ถ้าข้อมูลถูกต้อง ให้ดำเนินการสร้าง
# #         self.perform_create(serializer)

# #         return Response(serializer.data, status=status.HTTP_201_CREATED)


# # class FolderDetailView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Folder.objects.all()
# #     serializer_class = FolderSerializer
# #     permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from .models import Folder
# from .serializers import FolderSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()  # นำโมเดลผู้ใช้มาใช้งาน

# class FolderListCreateView(generics.ListCreateAPIView):
#     serializer_class = FolderSerializer
#     permission_classes = [AllowAny]  # ปรับแต่ง permission ตามความเหมาะสม

#     def get_queryset(self):
#         user_id = self.kwargs.get('user_id')  # รับ user_id จาก URL
#         if user_id:
#             return Folder.objects.filter(user__id=user_id)  # คืนค่าโฟลเดอร์ที่สัมพันธ์กับ user_id ที่ระบุ
#         return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์

#     def create(self, request, *args, **kwargs):
#         folder_name = request.data.get('folder_name')
#         user_id = request.data.get('user')  # เปลี่ยนเป็น user_id

#         print(f"Received folder_name: {folder_name}, user_id: {user_id}")

#         # ตรวจสอบว่า user_id ถูกส่งมาหรือไม่
#         if not user_id:
#             return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # ค้นหาผู้ใช้จาก user_id
#         try:
#             user = User.objects.get(id=user_id)
#             print(f"Found user: {user.username}")
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         # สร้างโฟลเดอร์พร้อมกับเชื่อมโยงกับ user_id ที่พบ
#         folder_data = {
#             "folder_name": folder_name,
#             "user": user.id  # บันทึกเป็น user_id
#         }

#         serializer = self.get_serializer(data=folder_data)

#         # ตรวจสอบความถูกต้องของ serializer
#         if not serializer.is_valid():
#             print(serializer.errors)  # พิมพ์ข้อผิดพลาด
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ส่งกลับข้อผิดพลาด

#         # ถ้าข้อมูลถูกต้อง ให้ดำเนินการสร้าง
#         self.perform_create(serializer)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# class FolderDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FolderSerializer
#     permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ

#     def get_queryset(self):
#         return Folder.objects.all()  # คืนค่าทุกโฟลเดอร์

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Folder
from .serializers import FolderSerializer
from django.contrib.auth import get_user_model

User = get_user_model()  # นำโมเดลผู้ใช้มาใช้งาน

class FolderListCreateView(generics.ListCreateAPIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]  # ปรับแต่ง permission ตามความเหมาะสม

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  # รับ user_id จาก URL
        if user_id:
            return Folder.objects.filter(user__id=user_id)  # คืนค่าโฟลเดอร์ที่สัมพันธ์กับ user_id ที่ระบุ
        return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์

    def create(self, request, *args, **kwargs):
        folder_name = request.data.get('folder_name')
        user_id = request.data.get('user')  # เปลี่ยนเป็น user_id

        # ตรวจสอบว่า user_id ถูกส่งมาหรือไม่
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # ค้นหาผู้ใช้จาก user_id
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # สร้างโฟลเดอร์พร้อมกับเชื่อมโยงกับ user_id ที่พบ
        folder_data = {
            "folder_name": folder_name,
            "user": user.id  # บันทึกเป็น user_id
        }

        serializer = self.get_serializer(data=folder_data)

        # ตรวจสอบความถูกต้องของ serializer
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ส่งกลับข้อผิดพลาด

        # ถ้าข้อมูลถูกต้อง ให้ดำเนินการสร้าง
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FolderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ

    def get_queryset(self):
        return Folder.objects.all()  # คืนค่าทุกโฟลเดอร์

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
