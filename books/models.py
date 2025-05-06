from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=10) 
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  
    total_pages = models.PositiveIntegerField(default=100)
    content = models.TextField(default="This is the default content for the book. ===PAGE=== Add more content here.")


    def __str__(self):
        return self.title

    def is_available(self):
        return self.stock > 0

    def borrow_count(self):
        return self.borrowing_set.count()  
    
    def get_pages(self):
        return self.content.split('===PAGE===')

    def get_page_range(self, start, end):
        return self.get_pages()[start:end]

