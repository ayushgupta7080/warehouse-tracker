# 📦 Warehouse Tracker MVP (Django)

This is a basic Django-based Warehouse Tracker application designed to manage and track product stock movement within a small warehouse. It includes product management, stock entries, and detailed tracking using three main tables.

## 🔧 Features

- Add, update, and view product details.
- Track incoming and outgoing stock.
- Maintain detailed history of each stock movement.
- Automatically updates product quantity based on stock in/out entries.

---

## 🗃️ Database Models

### 1. `prodmast` (Product Master)
- Stores product information like name, price, and image.
- Fields: `prodid`, `prodname`, `price`, `image`

### 2. `stckmain` (Stock Main)
- Tracks each stock transaction with a date and type (In/Out).
- Fields: `txnid`, `txndate`, `txntype` (In/Out)

### 3. `stckdetail` (Stock Details)
- Stores quantity of each product in a transaction.
- Foreign keys to both `prodmast` and `stckmain`.

---


## 🚀 Getting Started

### 📁 Clone the Repository 🐍 Set up Virtual Environment


🐍 Set up Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

📦 Install Dependencies
pip install -r requirements.txt

🔧 Apply Migrations
python manage.py makemigrations
python manage.py migrate


 Run the Server
 python manage.py runserver
Then open http://127.0.0.1:8000 in your browser.


Folder Structure

warehouse-tracker/
├── warehouse_project/      # Main Django project folder
│   ├── settings.py
│   └── urls.py
├── warehouse_app/          # App folder with models and views
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── media/                  # Uploaded product images
├── db.sqlite3              # Local database (optional)
├── requirements.txt
└── README.md


✍️ Author
Ayush Gupta
GitHub: @ayushgupta7080


---
📜 License
This project is open-source and free to use for educational and demo purposes.

Let me know if you'd like to add screenshots, a video demo link, or deployment instructions later — I can help you update the `README.md` anytime.



Due to a shortage of time, I was unable to deploy the project on platforms like Render or PythonAnywhere.
However, the complete source code is available on GitHub and can be run locally using the instructions provided in the README file.
If deployment is necessary or preferred, I would be happy to deploy it and share the live link—please let me know.
