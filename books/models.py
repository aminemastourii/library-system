from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=10) 
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # Add this field


    def __str__(self):
        return self.title

    def is_available(self):
        return self.stock > 0

    def borrow_count(self):
        return self.borrowing_set.count()  # related_name from Borrowing model

