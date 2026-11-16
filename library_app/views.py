from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from library_app.models import Book
from library_app.serializers import BookSerializer

# Create your views here.

class BookListCreateView(CreateAPIView,ListAPIView):
    queryset=Book.objects.all()
    serializerclass=BookSerializer


class BookDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Book.objects.all()
    serializerclass=BookSerializer
