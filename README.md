# 🏛 Bagh Ferdows Tehran Website

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-success?logo=django)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript)
![License](https://img.shields.io/badge/License-MIT-yellow)

Bagh Ferdows Tehran Website is a **practice project focusing on backend development** for the historical and cultural sites of the Bagh Ferdows complex. The frontend is **basic and minimal**. Users can register, share experiences, view others' stories, and purchase visit tickets. All content is **fully manageable via the Django admin panel**.

---

## 🚀 Key Highlights

* Fully dynamic content management via Django admin
* User registration and authentication
* Ticket booking and management
* Experience sharing and viewing other users' stories
* Basic frontend with minimal styling

---

## 🧠 Technologies

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** MySQL

---

## ⚙️ Features

### 👤 User Features

* User registration & login
* Share experiences and view other users' stories
* Browse locations with visiting rules and hours

### 💳 Ticketing

* Purchase visit tickets online
* View purchased tickets and booking history

### 🛠️ Admin Panel

* Add and manage locations dynamically
* Configure visiting rules and ticket availability
* Monitor user activity and experiences

---

## 🧩 Installation & Setup

### 1️⃣ Clone the project

```bash
git clone https://github.com/MohammadSalkhorde/bagh-ferdows-website.git
cd bagh-ferdows-website
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the database

Set your database credentials in `.env` or `settings.py`:

```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

### 5️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

> Access the application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📁 Project Structure

```
bagh-ferdows-website/
│
├── garden/
│   ├── apps/
│   ├── static/
│   ├── media/
|   ├── gerden/
│   └── templates/
│   └── manage.py
│
├── venv/
├── README.md
├── .env.example
└── requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💼 Contact & Portfolio

Hi, I'm **Mohammad Salkhorde** 👋
**Python / Django Backend Developer** — building dynamic websites and web applications. Open to **freelance** & **remote** opportunities.

* **GitHub:** [https://github.com/MohammadSalkhorde](https://github.com/MohammadSalkhorde)
* **LinkedIn:** [https://www.linkedin.com/in/mohammad-salkhorde-a13767385](https://www.linkedin.com/in/mohammad-salkhorde-a13767385)
* **Portfolio:** [https://mohammad-salkhorde.ir](https://mohammad-salkhorde.ir)
* **Email:** [m.salkhorde444@gmail.com](mailto:m.salkhorde444@gmail.com)
