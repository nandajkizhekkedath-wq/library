from rest_framework import serializers
from library_app.models import Book,BorrowRecorde


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'

class BorrowRecorde(serializers.ModelSerializer):
    class Meta:
        model =BorrowRecorde
        fields = '__all__'