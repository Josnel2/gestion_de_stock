from .models import User, OneTimePasscode
from .serializers import LogoutUserSerializer, UserRegisterSerializer, VerifyEmailSerializer, UserLoginSerializer, SetNewPasswordSerializer, PasswordResetRequestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from .utils import send_code_to_user
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .permissions import IsOwnerOrReadOnly, IsStaff, IsUser
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.core.cache import cache

class UserRegisterView(GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            send_code_to_user(user["email"])

            return Response({
                'data' : user,
                'message' : _(f'User {user['first_name']} created successfully, and code has be sent to your email'),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailView(GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        code = request.data.get("code")
        try:
            user_code_obj = OneTimePasscode.objects.get(code=code)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    'message' : 'account email verified succesfully'
                }, status=status.HTTP_200_OK)
            return Response({
                'message' : 'code us invalid user already verified'
            }, status=status.HTTP_204_NO_CONTENT)
        except OneTimePasscode.DoesNotExist:
            return Response({
                'message':'passcode not provided'
            }, status=status.HTTP_404_NOT_FOUND)
        
class LoginUserView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)

        return Response({
            'message':'a link has been send to your email to reset your password'
        }, status=status.HTTP_200_OK)
    
class PasswordResetConfirm(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    'message': _('token is invalid or has expired')
                }, status=status.HTTP_401_UNAUTHORIZED)
            return Response({
                'success': True,
                'message':'credential is valid',
                'uidb64': uidb64,
                'token':token,
            },status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError:
            return Response({
                'message':'token is invalid or has expired'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
class SetNewPasswordView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response({
            'message':'password reset successfully'
        }, status=status.HTTP_200_OK)

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsUser, IsStaff]

class LogoutUserView(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    """Session authentication"""
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    """Json Web Token authentication"""

class RefreshTokenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        tokens = user.tokens()
        cache.set("token", tokens)
        return Response(tokens)
 