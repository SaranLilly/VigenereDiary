from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import BlacklistMixin
from django.contrib.auth import get_user_model


from rest_framework.authtoken.models import Token


# user = User.objects.get(id=4)
# print(user)


# class UserListCreateView(generics.ListCreateAPIView):

#     User = get_user_model()

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         data = request.data.copy()
#         if 'password' in data:
#             data['password'] = make_password(data['password'])  # แฮชพาสเวิร์ดที่นี่

#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class UserListCreateView(generics.ListCreateAPIView):
    User = get_user_model()  # รับโมเดลผู้ใช้ที่กำหนดเอง

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        # แฮชพาสเวิร์ดที่นี่
        if 'password' in data:
            data['password'] = make_password(data['password'])  

        # สร้างผู้ใช้ใหม่ใน auth_user
        user = self.User(
            username=data['username'],
            password=data['password'],
            # เพิ่มฟิลด์อื่นๆ ที่จำเป็นจากโมเดลผู้ใช้
        )
        user.save()

        # หากคุณใช้ UserSerializer เพื่อส่งกลับข้อมูลผู้ใช้
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    User = get_user_model()

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        # เช็คว่ามีการส่งรหัสผ่านใหม่มาหรือไม่
        password = self.request.data.get('password', None)
        if password:  # ถ้ามีรหัสผ่านใหม่
            # แฮชรหัสผ่านใหม่
            serializer.validated_data['password'] = make_password(password)
        serializer.save()  # บันทึกข้อมูล


# class LoginView(APIView):
#     User = get_user_model()
#     User.objects.create_user(username='io', password='io')
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         try:
#             user = self.User.objects.get(username=username)
#         except self.User.DoesNotExist:
#             return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         if user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             serializer = UserSerializer(user)
#             return Response({
#                 "status": "success",
#                 "message": "Login successful",
#                 "id": user.id,
#                 "user": serializer.data,
#                 "access": str(refresh.access_token),
#                 'refresh': str(refresh),
                
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    User = get_user_model()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # # ตรวจสอบว่าผู้ใช้มีอยู่แล้ว ถ้ายังไม่มีให้สร้างใหม่
        # if not self.User.objects.filter(username=username).exists():
        #     self.User.objects.create_user(username=username, password=password)

        try:
            user = self.User.objects.get(username=username)
        except self.User.DoesNotExist:
            return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            return Response({
                "status": "success",
                "message": "Login successful",
                "id": user.id,
                "user": serializer.data,
                "access": str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


           

# class LoginView(APIView):
#     User = get_user_model()

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         try:
#             user = self.User.objects.get(username=username)
#         except self.User.DoesNotExist:
#             return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

#         # ตรวจสอบรหัสผ่าน
#         if user.check_password(password):  # ใช้ check_password ของโมเดลผู้ใช้
#             return Response({
#                 "status": "success",
#                 "message": "Login successful",
#                 "id": user.id,
#                 "username": user.username,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)







class LogoutView(APIView):
    User = get_user_model()
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            token = request.data.get('refresh')
            if not token:
                return Response({"status": "error", "message": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            # สร้าง RefreshToken object
            token_obj = RefreshToken(token)
            user_id = token_obj['user_id']  # ใช้ dict-style access เพื่อลงข้อมูลของ user_id

            if user_id:
                user = self.User.objects.get(id=user_id)  # หา user ที่เกี่ยวข้อง
                # ป้องกันไม่ให้ token นี้สามารถใช้งานได้
                token_obj.blacklist()
                return Response({"status": "success", "message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response({"status": "error", "message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)