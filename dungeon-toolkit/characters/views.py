from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Character
from .serializers import CharacterSerializer
from django.contrib.auth import get_user_model


class UserCharactersView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Character.objects.filter(created_by=self.request.user)
