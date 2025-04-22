from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_characters': '/',
        'Search by Slug': '/?slug=character_slug',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)


class UserCharactersView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Character.objects.filter(created_by=self.request.user)


@api_view(['POST'])
def add_character(request):
    character = CharacterSerializer(data=request.data)

    if Character.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This character already exists')

    if character.is_valid():
        character.save()
        return Response(character.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_character(request, pk):
    character = Character.objects.get(pk=pk)
    data = CharacterSerializer(instance=character, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_character(request, pk):
    character = get_object_or_404(Character, pk=pk)
    character.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
