from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.


class ListList(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class DetailList(generics.RetrieveUpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CreateList(generics.CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class DeleteList(generics.DestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

