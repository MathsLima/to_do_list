# To Do List
Project developed in Python using the Django Framework, HTML, BootStrap and Sqlite3.

It is a to-do list project, where the user can register a new task, change it, delete it and complete it. Tasks are organized according to the closest due date.

The application is local, uses Django for web development, HTML language and FrameWork Bootstrp to create the page layout. For the database, local Sqlite3 was used.

cria o ambiente virtual: python -m venv .venv  

altera a privacidade do codigo: Set-Executionpolicy -Scope Process -ExecutionPolicy ByPass

ativa o ambiente virtual: .\.venv\Scripts\activate

cria a estrutura basica do projeto: django-admin startproject setup .

executa o ambiente django web: python manage.py runserver

cria a app: python manage.py startapp todos

migracao do sqlite:  python manage.py migrate
                     python manage.py makemigrations