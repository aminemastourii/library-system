# 📚 Django Library Management System

A simple Django-based library management system that allows users to browse, borrow, and manage books. It includes user authentication, stock control, borrowing rules, and profile management.

---

## 🚀 Features

- ✅ Book catalog with title, author, category, publish date, and image
- 📦 Stock management (auto-decrease on borrow)
- 👤 Custom user model with borrower role
- 🗓️ Borrowing system with 30-day default duration
- 🚫 Limit of 5 active borrowings per user
- 🧾 Borrower profile with birthday
- 🧠 Admin-friendly (Django Admin integration)

---

## 🧱 Models Overview

### `Book`

- `title`, `author`, `publish_date`, `category`
- `stock`: Positive integer with default value
- `image`: Optional cover image
- `is_available()`: Returns `True` if stock > 0
- `borrow_count()`: Returns number of times book was borrowed

### `User` (extends Django's `AbstractUser`)

- Adds `is_borrower`: Boolean flag

### `BorrowerProfile`

- Linked via OneToOne to `User`
- Includes `birthday`

### `Borrowing`

- Links `User` and `Book`
- Automatically sets `start_date` and `end_date` (30 days later)
- Enforces:
  - 📉 Decrease in stock
  - ❌ Prevent borrow if out of stock
  - 🚫 Max 5 active borrowings

---

## 🛠️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/aminemastourii/library-system.git
cd library-management
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open [http://localhost:8000/admin](http://localhost:8000/admin) to access the Django admin panel.

---

## 🖼️ Media Setup (for book images)

In `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

In `urls.py` (for development only):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📂 Project Structure

```
library-management/
│
├── books/               # Book model & logic
├── borrowings/          # Borrowing logic
├── users/               # Custom user and profiles
├── media/               # Uploaded book images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---
