from email import message
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import random


class DicesView(APIView):
    def get(self, request: HttpRequest, *args, **kwargs):
        try:
            number = int(request.GET.get('number', default=1))
            faces = int(request.GET.get('faces', default=20))
            bonus = int(request.GET.get('bonus', default=0))
            mark = str(request.GET.get('mark', default=''))
            
            if faces not in {4, 6, 8, 10, 12, 20, 100}:
                return Response({'error': 'Invalid dice type'}, status=400)
            
            results = [random.randint(1, faces) for _ in range(number)]
            total = sum(results) + bonus
            message = f"{' +'.join(results)} + {bonus} = {total}"
            return Response({'results': results, 'total': total, 'message': message})
        except ValueError:
            return Response({'error': 'Invalid parameters'}, status=400)
