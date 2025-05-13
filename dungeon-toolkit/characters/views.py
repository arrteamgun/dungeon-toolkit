from django.forms import ValidationError
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


class AddCharacterView(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def perform_create(self, serializer: CharacterSerializer):
        print('DATA: ', self.request.data)
        if Character.objects.filter(name=self.request.data['name'][0], created_by=self.request.data['created_by'][0]).exists():
            raise ValidationError(f'The Character already exists!')
        serializer.save()


class UpdateCharacterView(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Character updated successfully", "character": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_character(request, pk):
    character = Character.objects.get(pk=pk)
    data = CharacterSerializer(instance=character, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class DestroyCharacterView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Character '{instance.name}' has been deleted."},
            status=status.HTTP_204_NO_CONTENT
        )
