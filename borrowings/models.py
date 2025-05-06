from django.db import models
from django.utils import timezone
from datetime import timedelta
from books.models import Book
from users.models import User

class Borrowing(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now() + timedelta(days=30))
    pages_borrowed = models.PositiveIntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.book.stock <= 0:
            raise ValueError("Book not available")
        if Borrowing.objects.filter(borrower=self.borrower, end_date__gte=timezone.now()).count() >= 5:
            raise ValueError("Borrowing limit reached")
        self.book.stock -= 1
        self.book.save()
        super().save(*args, **kwargs)

    def is_active(self):
        return self.start_date <= timezone.now().date() <= self.end_date

    def time_left(self):
        return (self.end_date - timezone.now().date()).days

    