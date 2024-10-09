
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Folder
from .serializers import FolderSerializer
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.authtoken.models import Token




User = get_user_model()  # นำโมเดลผู้ใช้มาใช้งาน

class FolderListCreateView(generics.ListCreateAPIView):
    serializer_class = FolderSerializer
    # permission_classes = [AllowAny]  # ปรับแต่ง permission ตามความเหมาะสม
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
   

    # def get_queryset(self):
    #     user_id = self.kwargs.get('user_id')  # รับ user_id จาก URL
    #     if user_id:
    #         return Folder.objects.filter(user__id=user_id)  # คืนค่าโฟลเดอร์ที่สัมพันธ์กับ user_id ที่ระบุ
    #     return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')  # ใช้ query_params แทน kwargs
        if user_id:
            return Folder.objects.filter(user__id=user_id)  # คืนค่าโฟลเดอร์ที่สัมพันธ์กับ user_id ที่ระบุ
        return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์

    # def get_queryset(self):
    #     user_id = self.request.user.id  # Get the ID of the currently logged-in user
    #     print(f"user id: {user_id}")
        
    #     if user_id:
    #         return Folder.objects.filter(user__id=user_id)  # Return folders associated with the logged-in user
    #     return Folder.objects.all()


    

    # def get_queryset(self):
    #     user_id = self.kwargs.get('user_id')  # รับ user_id จาก URL
    #     print(f"user id: {user_id}")
    #     if user_id:
    #         folders = Folder.objects.filter(user__id=user_id)  # กรองโฟลเดอร์ตาม user_id
    #         if folders.exists():
    #             return folders  # ถ้าพบโฟลเดอร์ที่สัมพันธ์กับ user_id
    #         else:
    #             raise Http404(f"No folders found for user ID {user_id}")  # ถ้าไม่พบโฟลเดอร์ แสดงข้อความว่าไม่มี user id นี้
           
    #     return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์


    def create(self, request, *args, **kwargs):
        folder_name = request.data.get('folder_name')
        user_id = request.data.get('user')  # เปลี่ยนเป็น user_id
        print(f"user id: {user_id}")
        print(f"request id: {request}")
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
    # permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Folder.objects.all()  # คืนค่าทุกโฟลเดอร์

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  # รับ user_id จาก URL
        if user_id:
            folders = Folder.objects.filter(user__id=user_id)  # กรองโฟลเดอร์ตาม user_id
            if folders.exists():
                return folders  # ถ้าพบโฟลเดอร์ที่สัมพันธ์กับ user_id
            else:
                raise Http404(f"No folders found for user ID {user_id}")  # ถ้าไม่พบโฟลเดอร์ แสดงข้อความว่าไม่มี user id นี้
        return Folder.objects.all()  # ถ้าไม่มี user_id ให้คืนค่าทุกโฟลเดอร์


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
