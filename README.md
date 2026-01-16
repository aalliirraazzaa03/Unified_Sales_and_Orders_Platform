Unified Sales and Orders Platform

A full-stack Django project with multiple apps to manage products, customers, and orders.

Project Overview

The Unified Sales and Orders Platform is a multi-app Django web application designed to handle:

Product management (App1)

Customer management (App2)

Order management connecting products and customers (App3)

It demonstrates a complete, functional Django project with:

Models, Views, Forms, and Templates

Admin interface registration for all apps

Fully linked URLs across three apps

Clean, modular structure

Features

Add, view, and manage products

Add, view, and manage customers

Create orders linking products to customers

User-friendly templates for all apps

Fully functional admin panel for managing database entries

Project Structure
multi_app_project/
│
├─ manage.py
├─ multi_app_project/
│   ├─ __init__.py
│   ├─ settings.py
│   ├─ urls.py
│   ├─ asgi.py
│   └─ wsgi.py
│
├─ app1/  # Products
│   ├─ models.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ forms.py
│   ├─ admin.py
│   └─ templates/app1/
│       ├─ home.html
│       └─ add_product.html
│
├─ app2/  # Customers
│   ├─ models.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ forms.py
│   ├─ admin.py
│   └─ templates/app2/
│       ├─ home.html
│       └─ add_customer.html
│
├─ app3/  # Orders
│   ├─ models.py
│   ├─ views.py
│   ├─ urls.py
│   ├─ forms.py
│   ├─ admin.py
│   └─ templates/app3/
│       ├─ home.html
│       └─ add_order.html
│
└─ templates/  # Optional shared templates

Installation

Clone the repository

git clone <repo-url>
cd multi_app_project


Create a virtual environment and activate

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies

pip install django


Run migrations

python manage.py makemigrations
python manage.py migrate


Create superuser (for admin)

python manage.py createsuperuser


Run the server

python manage.py runserver


Access the app

http://127.0.0.1:8000/app1/ → Products

http://127.0.0.1:8000/app2/ → Customers

http://127.0.0.1:8000/app3/ → Orders

http://127.0.0.1:8000/admin/ → Admin panel

Usage

Navigate to each app’s URL to view or add entries

Orders must link existing products and customers

All forms include CSRF protection

Admin interface allows full database management

Dependencies

Python 3.9+

Django 5.2+

Contributing

Fork the repository

Create a new branch for your feature

Commit changes and push to your branch

Open a pull request

License

MIT License
