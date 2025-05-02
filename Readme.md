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

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/yourusername/librarysys.git
cd librarysys
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Create Superuser (for admin access)
bash
Copy
Edit
python manage.py createsuperuser
6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
🔍 Usage
Visit / to access the homepage.

Click “Get Started” to sign up.

After signing up, complete your profile.

You will then be redirected to your dashboard.

From the dashboard, you can view available books, borrow them, and see your history.

📷 Screenshots
You can add screenshots here once you’ve deployed or finalized the UI:

📄 Homepage with “Get Started”

👤 Signup and profile completion

📘 Book detail and availability

📊 Dashboard with borrowed books and history

📦 Requirements
If not already present, create a requirements.txt:

shell
Copy
Edit
Django>=4.0
Generate with:

bash
Copy
Edit
pip freeze > requirements.txt
✨ Optional Improvements
Email confirmation or password reset

RESTful API using Django REST Framework

Book cover images





