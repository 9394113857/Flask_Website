# 🚀 Flask Website

A beginner-friendly Flask web application built using **Factory Pattern**, **Blueprints**, **Service Layer**, **Bootstrap**, and **Responsive Design**.

This project demonstrates how to organize a Flask application using a clean and scalable folder structure similar to professional backend applications while also showcasing a complete **DevOps workflow** using **Docker**, **GitHub Actions CI/CD**, **Docker Hub**, and **Render Deployment**.

---

## 🌐 Live Application

- 🌍 **Website:** [https://flask-website-service.onrender.com](https://flask-website-service.onrender.com)

## ❤️ Health Endpoint

- ❤️ **Health Endpoint:** [https://flask-website-service.onrender.com/health](https://flask-website-service.onrender.com/health)

The Health Endpoint displays:

- 🟢 Service Status
- 📦 Running Version
- 🔖 Git Commit SHA
- 🌿 Source Branch
- 🕒 Build Time (UTC)
- 🇮🇳 Build Time (IST)

### Why is this useful?

The build metadata is automatically generated during the **GitHub Actions CI Pipeline**, embedded into the **Docker Image**, deployed through **Render**, and exposed at runtime.

This makes it easy to verify exactly which version of the application is currently running in production.

---

# 📚 Features

- 🏠 Home Page
- 🧮 Calculator
- 📏 BMI Calculator *(Coming Soon)*
- ❤️ FLAMES Game *(Coming Soon)*
- 🎯 Guess Number Game *(Coming Soon)*
- ℹ️ About Page
- 📞 Contact Page
- ❤️ Runtime Health Endpoint
- 🐳 Dockerized Application
- ⚙️ GitHub Actions CI/CD
- 📦 Docker Hub Image Publishing
- ☁️ Render Deployment

---

# 🏗️ Project Architecture

```text
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

# 🚀 DevOps Deployment Flow

```text
Developer

        │

        ▼

Feature Branch

        │

        ▼

Pull Request

        │

        ▼

Merge Into Main

        │

        ▼

Git Version Tag

        │

        ▼

GitHub Actions CI

        │

        ├── Install Dependencies
        ├── Run Tests
        ├── Generate build_info.json
        ├── Build Docker Image
        ├── Push Version Image
        └── Push Latest Image

                │

                ▼

Docker Hub

                │

                ▼

Render Deployment

                │

                ▼

Docker Container

                │

                ▼

Flask Application

                │

                ▼

Health Endpoint

                │

                ▼

Runtime Build Metadata
```

---

# 📁 Project Structure

```text
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
├── .github/
│   └── workflows/
│        ci-flask-website.yml
│        cd-render-flask-website.yml
│
├── Dockerfile
├── requirements.txt
├── run.py
├── runtime.txt
├── README.md
└── build_info.json (Generated During CI)
```

---

# ⚙️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Jinja2
- Docker
- Git
- GitHub
- GitHub Actions
- Docker Hub
- Render

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

# 🌐 Local URLs

**Application**

http://127.0.0.1:5000

**Health Endpoint**

http://127.0.0.1:5000/health

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
| Health Endpoint | ✅ |

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
- Docker
- Git Workflow
- GitHub Actions CI
- Docker Image Creation
- Docker Hub Image Publishing
- Render Deployment
- Runtime Build Metadata
- Production Health Monitoring

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
- Role-Based Authorization
- API Documentation
- Monitoring & Logging
- Kubernetes Deployment

---

# 👨‍💻 Author

Built for learning **Flask Architecture**, **Backend Development**, **Docker**, **CI/CD**, and modern **DevOps Practices** using a clean, scalable, and production-inspired project structure.
