# 🍭 Sweet Shop Management System

The Sweet Shop Management System is a full-stack web application built to streamline the operations of a traditional sweet store. Developed using Django REST Framework (DRF) for the backend and React.js with Tailwind CSS for the frontend, this system adheres to Test-Driven Development (TDD) principles and clean coding practices.

This project empowers both administrators and end-users with robust features. Admins can manage sweets — add, update, delete, and restock items — while users can explore available sweets, make purchases, and search based on name and price. The system is secured using JWT (JSON Web Token) authentication, allowing for protected and role-based access to specific endpoints.

Whether you’re a developer looking to build a production-ready e-commerce backend or a sweet shop owner aiming to digitize your store, this system provides a modular, scalable, and API-first solution that's easy to maintain and extend.


---

## 🚀 Features

- 🔐 User Registration & JWT Login
- 🍬 Add / Update / Delete Sweets (Admin)
- 📃 List All Sweets
- 🛒 Purchase Sweets (User)
- 🔍 Search Sweets by Name & Price Range
- 📦 Restock / Low Stock Filtering

---

## 🛠️ Tech Stack

| Layer     | Technology               |
|-----------|--------------------------|
| Backend   | Django, Django REST Framework |
| Auth      | JWT (via SimpleJWT)      |
| Frontend  | React + Tailwind CSS     |
| Database  | SQLite (default)         |

---

## 📦 Backend (Django)

The backend of the Sweet Shop Management System is developed using Django and the Django REST Framework (DRF). It provides a secure, modular, and RESTful API architecture that handles user authentication, sweet inventory management, purchasing, and stock updates. Using JWT (via SimpleJWT) for authentication ensures that only authorized users can access or modify protected resources. The backend follows Test-Driven Development (TDD), with comprehensive unit tests covering all critical endpoints and logic.

---

```bash
git clone https://github.com/your-username/sweet-shop.git
cd sweetshop
python -m venv env
env\Scripts\activate  # On Windows
source env/bin/activate  # On Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 💻 Frontend (React)

The frontend is built using React.js, providing a fast, dynamic, and user-friendly interface for the sweet shop. Styled with Tailwind CSS, the UI is clean, responsive, and easily customizable. The frontend interacts with the backend API to support user registration/login, sweet browsing, purchasing, and admin controls. It consumes the DRF API through Axios and includes real-time feedback (e.g., toast messages) for smooth user interaction.

---

cd frontend
npm install
npm start

---

👑 Admin User (Optional)

python manage.py createsuperuser
Access admin dashboard at: http://localhost:8000/admin/

---

🔐 API Authentication (JWT)

| Method | Endpoint              | Description     |
| ------ | --------------------- | --------------- |
| POST   | `/api/auth/register/` | Register User   |
| POST   | `/api/auth/token/`    | Login (Get JWT) |

Use JWT token in header for protected routes:
Authorization: Bearer <access_token>

---

📋 API Endpoints

| Method | Endpoint                         | Description                |
| ------ | -------------------------------- | -------------------------- |
| POST   | `/sweet/add/`                    | Add new sweet (Admin only) |
| GET    | `/sweet/all/`                    | List all sweets            |
| GET    | `/sweet/<id>/`                   | Get sweet by ID            |
| PATCH  | `/sweet/<id>/update/`            | Update sweet (Admin only)  |
| DELETE | `/sweet/<id>/delete/`            | Delete sweet (Admin only)  |
| POST   | `/sweet/<id>/purchase/`          | Purchase sweet (User)      |
| POST   | `/sweet/<id>/restock/`           | Restock sweet (Admin only) |
| GET    | `/sweet/low-stock/`              | View low stock sweets      |
| GET    | `/sweet/in-stock/`               | View all available sweets  |
| GET    | `/sweet/search/?name=&min=&max=` | Search sweets              |

---


🧪 Running Tests (TDD)
python manage.py test

🤖 AI-Powered Development
✅ Guided TDD using Red → Green → Refactor cycle

✅ Auto-suggested Django REST patterns

✅ Helped with debugging & optimizing test coverage

✅ AI-assisted commit messages (co-authored)
