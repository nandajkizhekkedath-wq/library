from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from library_app.models import Book,BorrowRecorde
from library_app.serializers import BookSerializer,BorrowRecorded1

# Create your views here.

class BookListCreateView(CreateAPIView,ListAPIView):
    queryset=Book.objects.all()
    serializerclass=BookSerializer


class BookDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Book.objects.all()
    serializerclass=BookSerializer


class BorrowListCreateView(CreateAPIView,ListAPIView):
    serializer_class=BorrowRecorded1
    queryset=BorrowRecorde.objects.all()

class BorrowDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=BorrowRecorde
    queryset=BorrowRecorde.objects.all()



    