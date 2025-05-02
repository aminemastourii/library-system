# 📚 Library System with Borrowing History

A Django-based web application to manage books, authors, and borrowing records in a library. This project is developed as part of a semester evaluation to demonstrate practical knowledge of Django fundamentals, including models, CRUD operations, and templating.

---

## ✨ Features

- 📖 Manage a collection of books and authors
- 👤 Each book is associated with one author
- 🔄 Track borrowing and return history of books
- 📅 View which books are currently borrowed
- 🧾 Full CRUD (Create, Read, Update, Delete) for all entities
- 🖥️ Clean and user-friendly web interface

---

## 🗂️ Data Models

### Author

- `name`: Full name of the author
- `bio`: Short biography

### Book

- `title`: Title of the book
- `ISBN`: International Standard Book Number
- `publication_year`: Year of publication
- `author`: Foreign key to Author

### BorrowRecord

- `book`: Foreign key to Book
- `borrower_name`: Name of the person borrowing the book
- `borrowed_at`: Date and time when the book was borrowed
- `returned_at`: Nullable date/time field for when the book was returned

---

## 🎯 Objective

This project was built to:

- Practice designing and connecting related Django models
- Implement full CRUD functionality using Django’s generic views and forms
- Build a clean, navigable web interface using templates and views
- Simulate a real-world development workflow in a team-based setting

---

👥 Team Project
This project was developed as part of a group assignment. Each team was randomly assigned a topic, and this system was chosen to showcase Django skills in a collaborative environment.

🛠️ Technologies Used
Python 3.x

Django

SQLite (default DB)

HTML/CSS (Django templating)
Future Improvements
User authentication for borrowers

Pagination and search for books

Book categories or genres

Overdue book notifications

📄 License
This project is part of an academic assignment and is intended for educational use.
