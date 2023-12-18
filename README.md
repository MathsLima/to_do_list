# To Do List
Project developed in Python using the Django Framework, HTML, BootStrap and Sqlite3.

It is a to-do list project, where the user can register a new task, change it, delete it and complete it. Tasks are organized according to the closest due date.

The application is local, uses Django for web development, HTML language and FrameWork Bootstrp to create the page layout. For the database, local Sqlite3 was used.

Basic Commands:

creates the virtual environment: python -m venv .venv

changes code privacy: Set-Executionpolicy -Scope Process -ExecutionPolicy ByPass

activates the virtual environment: .\.venv\Scripts\activate

creates the basic project structure: django-admin startproject setup .

runs the django web environment: python manage.py runserver

create the app: python manage.py startapp all

sqlite migration: python manage.py migrate
                      python manage.py makemigrations