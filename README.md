# 🚀 Flask Website

A beginner-friendly Flask web application built using **Factory Pattern**, **Blueprints**, **Service Layer**, **Bootstrap**, and **Responsive Design**.

This project demonstrates how to organize a Flask application using a clean and scalable folder structure similar to professional backend applications.

---

# 📚 Features

- 🏠 Home Page
- 🧮 Calculator
- 📏 BMI Calculator *(Coming Soon)*
- ❤️ FLAMES Game *(Coming Soon)*
- 🎯 Guess Number Game *(Coming Soon)*
- ℹ️ About Page
- 📞 Contact Page

---

# 🏗️ Project Architecture

```
Browser
    │
    ▼
Controller
    │
    ▼
Service
    │
    ▼
Template (HTML)
    │
    ▼
Browser
```

---

# 📁 Project Structure

```
Flask_Website/
│
├── app/
│   │
│   ├── controllers/
│   │     home_controller.py
│   │     calculator_controller.py
│   │     bmi_controller.py
│   │     flames_controller.py
│   │     guess_controller.py
│   │     about_controller.py
│   │     contact_controller.py
│   │
│   ├── services/
│   │     calculator_service.py
│   │
│   ├── templates/
│   │     base.html
│   │     home.html
│   │     calculator.html
│   │     bmi.html
│   │     flames.html
│   │     guess.html
│   │     about.html
│   │     contact.html
│   │
│   ├── static/
│   │     css/
│   │          style.css
│   │
│   ├── config.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Git
- GitHub

---

# 📌 Design Pattern

- Factory Pattern
- Blueprint Architecture
- Service Layer
- MVC (Simplified)

---

# ▶️ Installation

## Clone Repository

```bash
git clone <repository-url>
```

---

## Navigate to Project

```bash
cd Flask_Website
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python run.py
```

or

```bash
flask run --debug
```

---

# 🌐 Open Browser

```
http://127.0.0.1:5000
```

---

# 📷 Current Pages

| Page | Status |
|------|--------|
| Home | ✅ |
| Calculator | ✅ |
| BMI | 🚧 |
| FLAMES | 🚧 |
| Guess Number | 🚧 |
| About | ✅ |
| Contact | ✅ |

---

# 📚 Learning Objectives

This project demonstrates:

- Flask Factory Pattern
- Flask Blueprints
- Flask Routing
- Service Layer
- HTML Forms
- GET Requests
- POST Requests
- Bootstrap Layout
- Responsive Design
- Static Files
- Template Inheritance
- Error Handling
- Git Workflow

---

# 🚀 Future Enhancements

- BMI Calculator
- FLAMES Game
- Guess Number Game
- REST APIs
- SQLite
- PostgreSQL
- Flask-Migrate
- Authentication
- Docker
- Render Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

Built for learning Flask architecture and backend development using professional project structure.