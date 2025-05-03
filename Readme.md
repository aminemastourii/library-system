📚 Library Management System
This is a Django-based Library Management System that allows registered users to borrow books, track their borrowing history, and manage stock availability. It includes basic user authentication and role-based functionality.

🚀 Features
📖 Add and manage books with cover images, categories, and stock count.

👥 Custom user model with borrower identification.

📅 Borrowing system with automatic due dates.

📉 Stock auto-decreases on borrow and prevents borrowing if out of stock.

🚫 Borrowing limit enforced (max 5 active borrowings).

🧠 User profiles with extra details like birthday.

🛠️ Tech Stack
Backend: Django 4.x

Database: SQLite (default) or any Django-supported DB

Media Handling: Django ImageField for book covers

Authentication: Django's built-in auth system (extended)

🧩 Models Overview
Book
Represents a book in the library.

Field Description
title Title of the book
author Author's name
publish_date Publication date
category Category/genre
stock Number of available copies
image Optional book cover image

📌 Includes:

is_available() to check if stock > 0

borrow_count() to return number of times borrowed

User
Custom user model (inherits from AbstractUser) with an additional field:

Field Description
is_borrower Boolean to identify borrower users

BorrowerProfile
Extra user details.

Field Description
birthday Date of birth

Borrowing
Tracks each book borrowing instance.

Field Description
borrower FK to User
book FK to Book
start_date Date of borrowing (default: today)
end_date Date due (default: today + 30 days)

📌 Logic includes:

Prevents borrowing if book stock is 0

Enforces a borrowing limit of 5 active borrowings per user

Reduces book stock upon borrowing

📷 Media & Static Files
To handle book cover images:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
Make sure to configure urls.py to serve media in development.

🧪 Running the App Locally
Clone the repository

git clone https://github.com/aminemastourii/library-system.git
cd library-management
Create a virtual environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Apply migrations

python manage.py makemigrations
python manage.py migrate
Create a superuser

python manage.py createsuperuser
Run the server

python manage.py runserver
📬 API (Optional Enhancement)
If you plan to expose this as an API in the future, consider adding:

Django REST Framework for API endpoints

Token-based authentication for mobile apps or external clients

📄 License
MIT License. You’re free to use, modify, and share.
