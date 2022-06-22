from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import re
import datetime
from datetime import timezone
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()
    
        
    #def check_password_expiry(user):
        
    #def disable_sessions(user): 
        
    
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    def get_roles(self, obj):
        user = User.objects.get(email=obj['email'])
        return user.role
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens',]
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        today = datetime.datetime.now(timezone.utc)
        account_dormancy = 90
        password_expired=45
        def days_between(d1, d2):
            delta = d1 - d2
            return(abs(delta.days))
        if not user:
            raise AuthenticationFailed('Invalid Credentials. Please Try Again.')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled. Please Contact Administrator.')
        #if not user.is_verified:
            #raise AuthenticationFailed('Email Not Verified. Please Contact Administrator.')
        if user:
            last_login=user.last_login
            last_password_change=user.last_password_change
            next_password_change=user.next_password_change
            if days_between(last_login,today)==account_dormancy:
                raise AuthenticationFailed('Account Dormant. Please Contact Administrator.')
            if next_password_change==today:
                raise AuthenticationFailed('Your Password is Expired. Please Reset Your Password To Proceed.')
            else:
                user.last_login=today
                user.save()
            pass
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        return super().validate(attrs)