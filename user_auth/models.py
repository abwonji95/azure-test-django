from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
class UserManager(BaseUserManager):
    def create_user(self,username,email,password,first_name,last_name,mobile,department,role,location):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Users should have a password')
        user=self.model(username=username,email=self.normalize_email(email),first_name=first_name,last_name=last_name,mobile=mobile,department=department,role=role,location=location,password=password)
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save()
        return user
    def create_superuser(self,username,email,password):
        if password is None:
            raise TypeError('Password cannot be empty')
        user=self.model(username=username,email=self.normalize_email(email),password=password)
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save()
        return user
class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=200,db_index=True,unique=True)
    first_name=models.CharField(max_length=200,db_index=True,blank=True)
    last_name=models.CharField(max_length=200,db_index=True,blank=True)
    mobile=models.CharField(max_length=200,db_index=True,blank=True)
    email=models.EmailField(max_length=200,db_index=True,unique=True)
    department=models.CharField(max_length=200,db_index=True,blank=True)
    role=models.CharField(max_length=200,db_index=True,blank=True)
    location=models.CharField(max_length=200,db_index=True,blank=True)
    password=models.CharField(max_length=200)
    is_verified=models.BooleanField(default=False)
    enable_2fa=models.BooleanField(default=False)
    enable_otp=models.BooleanField(default=False)
    auto_generate_password=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    last_login=models.DateTimeField(auto_now=True)
    last_password_change=models.DateTimeField(blank=True,null=True)
    next_password_change=models.DateTimeField(blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    search_fields = ('email',)
    objects = UserManager()
    def __str__(self):
        return self.email
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }