from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    isbn=models.CharField(max_length=50)
    available_copies=models.IntegerField

    def  __str__(self):
        self.title

class BorrowRecorde(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    borrower_name=models.CharField(max_length=50)
    borrower_email=models.EmailField()
    borrow_date=models.DateField(auto_now=True)
    is_returned=models.BooleanField(default=False)

    def __str__(self):
        return self.borrower_name
