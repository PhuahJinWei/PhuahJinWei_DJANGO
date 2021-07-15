from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import user
from . serializers import userSerializers

class userList(APIView):
    #Allow only GET method
    http_method_names = ['get']
    
    def get(self, request):
        buffer = user.objects.all()
        serializers = userSerializers(buffer, many = True)
        return Response(serializers.data)