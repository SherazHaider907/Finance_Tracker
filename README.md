# 📊 Finance Tracker (Django)

A **Personal Finance Management System** built with **Django** that allows users to track income, expenses, savings, and financial goals through a secure, user-specific dashboard.

---

## 🚀 Features

- User Registration & Authentication
- Add Income and Expense Transactions
- Categorize Transactions
- Create and Track Financial Goals
- Dashboard with:
  - Total Income
  - Total Expenses
  - Net Savings
  - Goal Progress
- Export Transactions to Excel (.xlsx)
- User-specific and secure data handling

---

## 🛠️ Tech Stack

- Python
- Django
- Django ORM
- Django Forms
- django-import-export
- SQLite (default database)

---

## 📁 Project Structure

Finance_Tracker/
├── finance/
│ ├── models.py # Transactions & Goals models
│ ├── forms.py # Django forms
│ ├── views.py # Application logic
│ ├── templates/
│ └── admin.py
├── manage.py
└── README.md

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/SherazHaider907/Finance_Tracker.git
cd Finance_Tracker

2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

4️⃣ Install Dependencies
pip install django
pip install django-import-export

5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Run Server
python manage.py runserver

Open browser:

http://127.0.0.1:8000/
