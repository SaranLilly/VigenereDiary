from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Diary
from .serializers import DiarySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.authtoken.models import Token



class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ
    def vigenere_encrypt(self, text, key):
        encrypted_text = []
        key = key.lower()
        key_index = 0

        for char in text:
            if char.isalpha():  # เข้ารหัสเฉพาะตัวอักษร
                shift = ord(key[key_index]) - ord('a')
                base = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - base + shift) % 26 + base)
                encrypted_text.append(encrypted_char)
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_text.append(char)

        return ''.join(encrypted_text)

    def perform_create(self, serializer):
        key = self.request.data.get('key', None)
        if not key:
            return Response({"error": "Encryption key is required"}, status=status.HTTP_400_BAD_REQUEST)

        content = serializer.validated_data.get('content')
        if content:
            encrypted_content = self.vigenere_encrypt(content, key)
            serializer.validated_data['content'] = encrypted_content

        serializer.save()

    def create(self, request, *args, **kwargs):
        if 'key' not in request.data:
            return Response({"error": "Encryption key is missing"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)



class DiaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [AllowAny]  # สามารถปรับให้เหมาะสมตามความต้องการ

    def vigenere_decrypt(self, text, key):
        decrypted_text = []
        key = key.lower()
        key_index = 0

        for char in text:
            if char.isalpha():  # ถอดรหัสเฉพาะตัวอักษร
                shift = ord(key[key_index]) - ord('a')
                base = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted_text.append(decrypted_char)

                key_index = (key_index + 1) % len(key)
            else:
                decrypted_text.append(char)

        return ''.join(decrypted_text)

    def retrieve(self, request, *args, **kwargs):
        # ดึงคีย์ถอดรหัสจาก request
        key = request.query_params.get('key', None)

        if not key:
            return Response({"error": "Decryption key is required"}, status=status.HTTP_400_BAD_REQUEST)

        # ดึง instance ของ Diary
        instance = self.get_object()

        # แสดงข้อความที่เข้ารหัสเพื่อเช็ค
        print(f"ข้อความที่เข้ารหัส: {instance.content}")

        # ถอดรหัสฟิลด์ content โดยใช้คีย์ที่ได้รับมา
        decrypted_content = self.vigenere_decrypt(instance.content, key)

        # แสดงข้อความที่ถอดรหัสเพื่อเช็ค
        print(f"ข้อความที่ถอดรหัส: {decrypted_content}")

        # แก้ไข instance content หลังถอดรหัส
        instance.content = decrypted_content

        # ส่งข้อมูลกลับหลังจากถอดรหัส
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DiaryDeleteView(generics.DestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]  # Set permissions as needed

    def destroy(self, request, *args, **kwargs):
        # Get the diary instance to be deleted
        instance = self.get_object()
        
        # Delete the diary entry
        instance.delete()

        # Return a response indicating successful deletion
        return Response({"message": "Diary entry deleted successfully."}, status=status.HTTP_204_NO_CONTENT)






