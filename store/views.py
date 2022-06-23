from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

import random
from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
#from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
#from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
#from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, HttpResponsePermanentRedirect
#from authentication.userthrottle import UserLoginRateThrottle
import datetime
#from .permissions import IsAdmin
from datetime import timezone
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def index(request):
    return render(request, 'store/home.html', context=None),

