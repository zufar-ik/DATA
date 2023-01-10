from django.shortcuts import render
from rest_framework import generics

from .models import News
from .serializers import NewsInfo


class NewsPUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsInfo


class NewsAPI(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsInfo
