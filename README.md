#  Hand Drawing to Digital Image Enhancement (Django)

A Django-based web application that converts hand-drawn images into enhanced digital outputs using image processing techniques.  
This project allows users to upload hand-drawn sketches and transform them into cleaner, clearer digital-style images.

---

##  Project Overview

This application is built using the Django web framework and provides:

- Image upload functionality
- Image enhancement processing
- Processed image display
- Static & template-based frontend
- SQLite database integration

The system is designed to improve low-quality hand-drawn images and convert them into enhanced digital versions suitable for further editing or presentation.

---

##  Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite3
- **Image Processing:** Python imaging libraries (OpenCV / PIL if used)
- **Version Control:** Git & GitHub

---

##  Project Structure

```
HandDrawing-to-Digital-Django/
│
├── manage.py
├── db.sqlite3
├── imageapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── imageenhance/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── .gitignore
└── README.md
```

---

##  Installation & Setup

Follow these steps to run the project locally:

### 1️. Clone the Repository

```bash
git clone https://github.com/RASHAD750/HandDrawing-to-Digital-Django.git
cd HandDrawing-to-Digital-Django
```

---

### 2️. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install django
```

---

### 4️. Apply Migrations

```bash
python manage.py migrate
```

---

### 5️. Run the Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

##  Features

 Upload hand-drawn image  
 Process and enhance image  
 Display enhanced output  
 Organized Django project structure  
 Database-backed application  

---

##  How It Works

1. User uploads a hand-drawn image.
2. The image is stored in the media/static folder.
3. Backend processing enhances clarity and sharpness.
4. Enhanced image is rendered back to the user interface.

---

##  Use Cases

- Converting sketches to digital format
- Improving scanned handwritten diagrams
- Academic project demonstrations
- Portfolio showcase project

---

##  .gitignore Configuration

The project ignores:

- Virtual environment folders
- SQLite database
- __pycache__
- VS Code settings
- OS system files

---

##  Future Improvements

- Add AI-based sketch enhancement (Deep Learning)
- Add user authentication system
- Deploy on cloud (Heroku / Render / AWS)
- Add image comparison view
- Download enhanced image option

---

