# ✨ Mezon Elmira | Online Boutique Web Application

![Django](https://img.shields.io/badge/Django-5.2-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Deployment](https://img.shields.io/badge/Deployment-Render-black)

A modern and responsive e-commerce web application developed for a women's fashion boutique.

The goal of this project was to build a complete online showcase platform where customers can explore products, browse categories, and view detailed information about each product.

🌐 **Live Demo:**
http://mezon-elmira.onrender.com/


---

## 📌 Project Overview

**Mezon Elmira** is a Django-based boutique website designed for presenting and managing luxury fashion products.

The project focuses on:

- Clean UI/UX design
- Product management
- Category-based browsing
- Search functionality
- Responsive design
- Django admin customization
- Production deployment


---

# 🚀 Features

## 👗 Product Management

- Product catalog
- Product detail pages
- Multiple product images support
- Product categories
- Color management
- Size management
- Inventory management
- Price management


## 🔎 Search & Filtering

- Product search by title
- Category-based product browsing
- Dynamic navigation menu


## 🛠 Admin Dashboard

Customized Django administration panel with:

- Product management
- Category management
- Color and size management
- Product image uploading
- Inventory editing
- Search and filtering tools


## 🎨 Frontend

The frontend was developed with:

- HTML5
- CSS3
- Bootstrap 5 RTL
- Responsive layouts
- Custom animations
- Modern luxury fashion design


## ⚙️ Backend

Built with Django framework:

- Django Models
- Django Views
- URL Routing
- Template inheritance
- Context processors
- Django Admin customization


---

# 🏗 Project Architecture

```
Mezon-Elmira/

│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── mezon/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── home.html
│   ├── product_list.html
│   ├── product_detail.html
│   ├── about_us.html
│   └── contact_us.html
│
├── static/
│
├── media/
│
├── requirements.txt
├── build.sh
└── manage.py

```


---

# 🧰 Technologies Used

## Backend

- Python
- Django


## Database

- SQLite (Development)


## Frontend

- HTML
- CSS
- Bootstrap


## Deployment

- Render
- Gunicorn
- WhiteNoise


---

# 🔐 Production Configuration

The project includes production-ready configurations:

- Environment variables using python-decouple
- DEBUG configuration separation
- Static file handling with WhiteNoise
- Gunicorn WSGI server
- Automated deployment build script


---

# 📦 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/realhesam04/Mezon-Elmira.git
```

Navigate to project directory:

```bash
cd Mezon-Elmira
```

Create virtual environment:

```bash
pip install pipenv
pipenv install
```

Activate environment:

```bash
pipenv shell
```

Run migrations:

```bash
python manage.py migrate
```

Create admin account:

```bash
python manage.py createsuperuser
```

Run development server:

```bash
python manage.py runserver
```


---

# 📸 Screenshots



---

# 👨‍💻 Developer

**Hesam Ehsani**

Software Engineering Student

Backend Developer focused on:

- Python
- Django
- REST API Development
- Web Applications


GitHub:

https://github.com/realhesam04


---

# 📄 License

This project was developed as a portfolio project for learning and demonstrating Django web development skills.
