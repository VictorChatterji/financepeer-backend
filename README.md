**Documentation**

1. This is backend codebase built in Django REST framework
2. create virtual environment
3. `python3 -m venv virtualenv-name`
4. cd `virtualenv-name`
5. Clone the project
6. `git clone https://gitlab.com/VictorChatterji/financepeer.git`
7. cd `financepeer`
8. Install the requirements
9. `pip3 install -r requirements.txt`
10. Configure the database in the `settings.py` file in the codebase
11. The database used for this project is `MYSQL`
12. In the `settings.py` file of your django project under `DATABASES` change
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

to

13. For windows users (Use WAMP)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME', # I used financepeer_json
        'USER': 'DB_USER', # normally root
        'PASSWORD': 'DB_PASSWORD', # normally empty string or root
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

14. For Mac or linux (USE XAMP or MAMP)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME', # I used financepeer_json
        'USER': 'DB_USER', # normally root
        'PASSWORD': 'DB_PASSWORD', # normally empty string or root
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '8889', # mac users (MAMP database port is running)
    }
}
```

15. Migrate the models to database
16. `python3 manage.py makemigrations`
17. `python3 manage.py migrate`

18. If you check the database. The database is populated with the tables from the project

19. `python3 manage.py createsuperuser` for creating the user to login inside the system

20. Finally `python3 manage.py runserver` to serve the application
