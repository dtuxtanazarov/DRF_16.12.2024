from django.shortcuts import render
from .serializers import New_serializer
from News.models import New
from rest_framework.views import APIView, Response
from rest_framework.generics import *
# Create your views here.
class List_view(ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = New_serializer

class Detail_view(RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = New_serializer


