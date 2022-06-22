from django.urls import path
from .views import *
from  . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
]