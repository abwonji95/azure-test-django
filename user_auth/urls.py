from django.urls import path
from .views import *
from  . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('', LoginView.as_view(), name="login"),
]