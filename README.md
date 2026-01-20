# Django CRUD Application 

A simple and clean **Django CRUD (Create, Read, Update, Delete)** project built for learning and practice.  
This project demonstrates Django fundamentals such as apps, models, views, URLs, and database operations.

## What This Project Does

- Create new records
- View existing records
- Update records
- Delete records
- Manage data using Django Admin

## Tech Stack

- **Python**
- **Django**
- **Postgres**
- **Virtual Environment**

## Project Structure

```
 
training-django/
├── project/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   └── crud/
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       └── urls.py
│
├── common/
├── venv/
├── requirements.txt
└── README.md

````

## ⚙️ Setup & Run

### Clone the repository
```bash
git clone https://github.com/abhishekk75way/training-django.git
cd training-django
````

### Activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
cd project
python manage.py migrate
```

### Start server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

## Admin Panel

Create admin user:

```bash
python manage.py createsuperuser
```

Admin URL:

```
http://127.0.0.1:8000/admin/
```