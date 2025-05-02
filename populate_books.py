import os
import django
import random
from faker import Faker
from datetime import date, timedelta
from django.core.files import File  # Import File for handling image uploads

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarysys.settings')
django.setup()

from books.models import Book

# Initialize Faker
fake = Faker()

# Directory containing available images
IMAGES_DIR = os.path.join('librarysys', 'media', 'books','images')

# Load all images from the directory
available_images = [
    f for f in os.listdir(IMAGES_DIR)
    if f.lower().endswith(('.jpeg', '.jpg', '.png'))
]

# List of categories
categories = ["Fiction", "Non-Fiction", "Science", "History", "Biography"]

def create_books(n):
    for _ in range(n):
        # Generate a random publish date within the last 50 years
        publish_date = date.today() - timedelta(days=random.randint(0, 50 * 365))

        # Select a random image
        image_name = random.choice(available_images)
        image_path = os.path.join(IMAGES_DIR, image_name)

        # Create a new book
        book = Book(
            title=fake.sentence(nb_words=3),
            author=fake.name(),
            publish_date=publish_date,
            category=random.choice(categories),  # Assign a random category
            stock=random.randint(1, 50),  # Random stock between 1 and 50
        )

        # Assign the image using Django's File object
        with open(image_path, 'rb') as image_file:
            book.image.save(image_name, File(image_file), save=True)

if __name__ == "__main__":
    create_books(100)
    print("100 books created with random images, categories, and publish dates!")