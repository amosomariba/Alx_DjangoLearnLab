# LibraryProject

LibraryProject is a Django-based web application. This project was generated using Django 5.2.4.

## Project Structure

```
LibraryProject/
    db.sqlite3
    manage.py
    README.md
    LibraryProject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

## Getting Started

### Prerequisites

- Python 3.10+
- Django 5.2.4 (install with `pip install django`)

### Setup

1. **Install dependencies:**

    ```sh
    pip install django
    ```

2. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

3. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

4. **Access the app:**

    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Admin Interface

To use the Django admin interface:

1. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

2. Access the admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Files

- `manage.py`: Django's command-line utility.
- `LibraryProject/settings.py`: Project settings.
- `LibraryProject/urls.py`: URL configuration.
- `LibraryProject/wsgi.py` and `asgi.py`: Deployment entry points.

## Django Admin Configuration for Book Model

### Admin Registration
The `Book` model is registered using the `@admin.register()` decorator in `bookshelf/admin.py`.

### Admin Customization
- `list_display`: Shows title, author, and publication year in the admin table.
- `list_filter`: Enables filtering by author and publication year.
- `search_fields`: Allows searching by book title or author name.

### Accessing Admin
- Run `python manage.py runserver`
- Open [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Log in with the superuser credentials
