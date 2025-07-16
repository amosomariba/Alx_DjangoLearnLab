# LibraryProject

LibraryProject is a Django-based web application template for managing library-related data. This project uses SQLite as its default database and includes Django's built-in admin interface.

## Features

- Django 5.2 project structure
- SQLite3 database for development
- Ready-to-use admin panel
- Easily extendable for custom library models and views

## Getting Started

### Prerequisites

- Python 3.10+
- Django 5.2+
- (Optional) Virtual environment

### Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   cd LibraryProject
   ```

2. (Optional) Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```sh
   pip install django
   ```

4. Apply migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser for admin access:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/)


