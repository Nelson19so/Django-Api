from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
# from rest_framework
from .serializer import BlogPostSerializer

# Create your views here.

class BlogPostSerializerCreate(generics.ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  lookup_field = "pk"