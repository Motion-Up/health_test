from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from tests.models import Test
from .serializers import TestSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]
