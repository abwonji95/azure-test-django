from django.urls import path
from .views import *
from  . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.index, name='index'),
]