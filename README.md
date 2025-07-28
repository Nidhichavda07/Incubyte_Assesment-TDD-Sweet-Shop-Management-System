 Sweet Shop Management System
A full-stack Sweet Shop app built using Django REST Framework and React.js, developed using Test-Driven Development (TDD) and clean code practices.

🚀 Features
🔐 User Registration & JWT Login

🍬 Add / Update / Delete Sweets

📃 List All Sweets

🛒 Purchase Sweets (end user)

🔍 Search by Name & Price Range

🛠️ Tech Stack
Layer	Tech
Backend	Django, DRF
Auth	JWT (SimpleJWT)
Frontend	React + Tailwind CSS
Database	SQLite (default)

🔧 Setup Instructions
📦 Backend (Django)

git clone https://github.com/your-username/sweet-shop.git
cd sweetshop
python -m venv env
env\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
💻 Frontend (React)
cd frontend
npm install
npm start
👑 Admin User (Optional)

python manage.py createsuperuser
🔐 API Auth
POST /api/auth/register/ → Register

POST /api/auth/token/ → Login (get JWT)

For protected routes:
Authorization: Bearer <access_token>
📋 API Endpoints
Method	Endpoint	Description
POST	/sweet/add/	Add new sweet
GET	/sweet/all/	List all sweets
GET	/sweet/<id>/	Get sweet by ID
PATCH	/sweet/<id>/update/	Update sweet
DELETE	/sweet/<id>/delete/	Delete sweet (admin)
POST	/sweet/<id>/purchase/	Purchase sweet
POST	/sweet/<id>/restock/	Restock sweet (admin)
GET	/sweet/low-stock/	View low stock items
GET	/sweet/in-stock/	View in-stock items
GET	/sweet/search/?name=&min_price=&max_price=	Search sweets

🧪 Running Tests (TDD)

python manage.py test
✅ Tests cover user auth, sweet CRUD, purchase/restock, stock filters, and search.

🤖 AI Usage
Guided TDD steps (Red → Green → Refactor)

Suggested Django patterns, helped debug test cases

Co-authored commits where AI was used

✅ Sample Output:
bash
Copy
Edit
Found 12 test(s).
Creating test database...
............
