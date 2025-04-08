from operator import imod
from re import S
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .models import User
from .forms import LoginUserForm
from .serializers import AuthStatusSerializer

from rest_framework.views import APIView

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model


# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class AuthCheckView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = AuthStatusSerializer({"status": "АВТОРИЗОВАН"})
        return Response(serializer.data)

    def permission_denied(self, request, message=None, code=None):
        serializer = AuthStatusSerializer({"status": "НЕТ ДОСТУПА"})
        return Response(serializer.data, status=403)


class CurrentUserView(APIView):
    def get(self, request):
        user = request.user
        return Response(
            {
                'username': user.username,
                'email': user.email
            }
        )
