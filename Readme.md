# 📚 Library Management System

A full-featured **Library Management System** built with Django. This project allows users to register, complete their profiles, browse and borrow books, return them (manually or automatically), and track their borrowing history. Admins can manage books and monitor user activity efficiently.

---

## 🚀 Features

### 👥 User Features
- User registration with profile completion
- Login/logout functionality
- Dashboard with:
  - Available books
  - Borrowed books
  - Borrowing history
- Borrow/return book functionality
- Enforced borrowing limits
- Automatic and manual return handling
- Book availability indicator
- Sort books by most borrowed or alphabetically
- Search books by title or category

### 🛠 Admin Features
- Full CRUD for books through the Django admin interface
- View and manage all users and borrowings
- Monitor book popularity based on borrowing frequency

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.x)
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)
- **Frontend:** HTML + optional CSS framework (Bootstrap or Tailwind)
- **Auth:** Django’s built-in authentication system

---

## 📁 Project Structure

librarysys/
├── books/ # Book app: models, views, templates
├── borrowings/ # Borrowing logic: models, views, templates
├── users/ # User registration, profile, auth
├── templates/ # Shared HTML templates
├── static/ # Static files (CSS, JS, images)
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md

yaml
Copy
Edit

---






