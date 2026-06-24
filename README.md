Django Recipe Management System

A modern Recipe Management System built with Django that allows users to register, log in, and manage recipes with full CRUD functionality.

## ✨ Features

### 🔐 Authentication System

* User Registration
* User Login
* Password Authentication
* Session Management
* Validation Messages

### 🍽️ Recipe Management

* Create Recipes
* View Recipe List
* Update Existing Recipes
* Delete Recipes
* Upload Recipe Images

### 🔍 Search Functionality

* Search recipes by name
* Real-time filtering using Django ORM

### 🎨 User Interface

* Responsive Bootstrap 5 Design
* Modern UI with Gradient Themes
* Clean and User-Friendly Layout
* Mobile-Friendly Design

---

## 🛠️ Tech Stack

### Backend

* Python 3
* Django 6

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite3 (Default Django Database)

### Authentication

* Django Authentication System

---

## 📂 Project Structure

```text
project/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── vege/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── recipies.html
│   └── recipe_update.html
│
├── media/
│   └── recipe/
│
├── manage.py
└── README.md
```

---

## 📊 Database Model

### Recipe Model

```python
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=40)
    recipe_description = models.TextField(max_length=250)
    recipe_image = models.ImageField(upload_to="recipe")

    def __str__(self):
        return self.recipe_name
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/django-recipe-management.git
```

### 2. Navigate to Project Folder

```bash
cd django-recipe-management
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install django pillow
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run Server

```bash
python manage.py runserver
```

### 8. Open Browser

```text
http://127.0.0.1:8000/login/
```

---

## 📸 Application Screens

### Login Page

* User Authentication
* Error Handling
* Bootstrap UI

### Registration Page

* New User Creation
* Username Validation
* Success Messages

### Recipe Dashboard

* Add New Recipes
* Search Recipes
* View Uploaded Images
* Delete Recipes
* Update Recipes

---

## 🔗 Available Routes

| Route                | Description       |
| -------------------- | ----------------- |
| /login/              | User Login        |
| /register/           | User Registration |
| /recipe/             | Recipe Dashboard  |
| /update_recipe/<id>/ | Update Recipe     |
| /delete_recipe/<id>/ | Delete Recipe     |

---

## 🎯 Future Improvements

* Logout Functionality
* User Profile Page
* Pagination
* Recipe Categories
* Recipe Likes
* Comments System
* REST API using Django REST Framework
* JWT Authentication
* Docker Deployment
* PostgreSQL Database

---

## 👨‍💻 Learning Outcomes

This project demonstrates:

* Django MVT Architecture
* URL Routing
* Django ORM
* CRUD Operations
* Authentication & Authorization
* File/Image Upload Handling
* Bootstrap Integration
* Template Rendering
* Form Processing
* Search Functionality

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Muhammad Huzaifa

Built with ❤️ using Django and Bootstrap.
