from rest_framework import serializers
from library_app.models import Book,BorrowRecorde


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = '__all__'

class BorrowRecorded1(serializers.ModelSerializer):
    class Meta:
        model =BorrowRecorde
        fields = '__all__'

    def validate_book(self,book):
        if book.available_copies==0:
            raise serializers.ValidationError("book is not available")
        return book