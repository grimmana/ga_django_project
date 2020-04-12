# ga_django_project
Project Link: GitHub- https://github.com/grimmana/ga_django_project

# Project Description:
This application allows users to store part number information for their various possessions. 

Features:
- Have two related models.
- Implement Full CRUD throughout the application
- Utilizes user authentication and routes that require login for access.


Technologies used:
Python
SQL
Django
GitHub
NodeJS
WireFrame

Deployment to Heroku 
Code Snippet:
Issues and resolutions:
Contribute
## Additional Resources

- [Django Docs: Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
- [Django Docs: Models & Databases](https://docs.djangoproject.com/en/2.0/topics/db/)
- [How to Create Django Models](https://www.digitalocean.com/community/tutorials/how-to-create-django-models)
- [Django Docs: Migrations](https://docs.djangoproject.com/en/2.0/topics/migrations/)
- [Django Docs: Writing Database Migrations](https://docs.djangoproject.com/en/2.0/howto/writing-migrations/)
- [Django Docs: Admin](https://docs.djangoproject.com/en/2.1/ref/django-admin/)
- [Django Docs: Providing initial data for models](https://docs.djangoproject.com/en/2.1/howto/initial-data/)
- [Django Extensions](https://github.com/django-extensions/django-extensions)




# Installation Instructions 

<!-- This section should walk a reader, step by step, through the process of setting up your project
For a tool meant to be integrated into other projects, this would likely outline the process of installing and accessing this tool in your project
For an application, this would likely outline the process of forking, cloning, and starting the app locally -->

# Getting Started
1. Create a new repository on your personal GitHub account 
2. Fork and clone down this repository.


# Set up the Django application
Create a directory for the application on your computer:

```sh
mkdir part_django
```

Then, `cd` into the `part_django/` folder you created.

Run the following commands to set up the virtual environment:

```sh
python3 -m pip install virtualenv
python3 -m venv .env
source .env/bin/activate
```

The command `source .env/bin/activate` activates the virtual environment. Remember to activate it each time you work on your project.


Install Django:

```
python3 -m pip install django 
```

If prompted that a more current version of pip is available; go ahead and run the upgrade

```
pip install --upgrade pip
```

Install the library to connect Django to PostgreSQL:

```
python3 -m pip install psycopg2-binary
```		

Start the Django project - 
> Make sure you put the `.` on the end! This creates the project in the current
> directory instead of creating a new subfolder.

```sh
django-admin startproject part_django .
```

Create the app:

```bash
$ django-admin startapp part
```

> Note: if django-admin doesn't work, you can replace it with
> `python3 manage.py`, assuming `manage.py` is in your current directory.


The application structure looks like this now:
 
- part_django 
    - .env
    - part
        - Migrations
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    - part_django
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manage.py
README.md


# Database Setup

Using pSQL

Login to `psql`:

```bash
$ psql -d postgres
```

Create a database:

```sql
> CREATE DATABASE part;
> CREATE USER partuser WITH PASSWORD 'part';
> GRANT ALL PRIVILEGES ON DATABASE part TO partuser;
> \q
```

Then, in `part_django/part_django/settings.py` find the `DATABASES` constant dictionary.
Update it to look like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'part',
        'USER': 'partuser',
        'PASSWORD': 'part',
        'HOST': 'localhost'
    }
}
```
Add the application `part` to the bottom line of the
 `INSTALLED_APPS` list.

 ```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'part'
]
```

In the terminal run `python3 manage.py runserver` then in the browser navigate to 
`localhost:8000`

You should see a page welcoming you to Django!

# Models

Create the class and add the fields and define the default method in: part_django/part/models.py

```python
# part_django/part/models.py
class Item(models.Model):
    name = models.CharField(max_length=100)
    ident = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
```

# Migrations 

Migrate the new model `Item` to the database:

Reminder: **NEVER** edit the migration files manually. Always, edit the models.py
file and then run the makemigrations command again.

```bash
$ python3 manage.py makemigrations
```

Run the next command after all the changes to the models file have been completed:

```bash
$ python3 manage.py migrate
```

Add `Item_part` to the models.py file. Create the class, add a foreign key, 
add additional fields and then define a default method in part_django/part/models.py 
(below the existing class Item):

```python
# part_django/part/models.py

class Item(models.Model):
    name = models.CharField(max_length=100)
    ident = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item_part(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_parts')
    part_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100) 
    part_notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
```

Another migration will need to be completed. 

```bash
$ python3 manage.py makemigrations
```

Run the migrate command, after all the changes to the models file have been completed:

```bash
$ python3 manage.py migrate
```

# Admin Console 

Create a superuser for the application. In the terminal, run:

```bash
$ python3 manage.py createsuperuser
```
Fill in the requested information as prompted.

# Seed database using the Admin Console

To use the Django admin dashboard with built-in
full CRUD functionality:

Add the following code to the file part_django/part/admin.py to register the
models `Item` 

```python
from .models import Item

admin.site.register(Item)

```
Another migration will need to be completed.

```bash
$ python3 manage.py makemigrations
```

Run the migrate command, after all the changes to the models file have been completed:

```bash
$ python3 manage.py migrate
```

In the browser go to the Admin Console http://localhost:8000/admin/

Manually add the seed data to `Items`

Return to VScode:

Add `Item_part` to the file part_django/part/admin.py in two places 
to register the model.

```python
from .models import Item, Item_part

admin.site.register(Item)
admin.site.register(Item_part)  
```
Another migration will need to be completed. 

```bash
$ python3 manage.py makemigrations
```

Run the migrate command, after all the changes to the models file have been completed:

```bash
$ python3 manage.py migrate
```

In the browser go to the Admin Console http://localhost:8000/admin/part/ to 
seed data using add `Item_parts`

# Django Extensions - 

Install additional debugging functionality to Django.

```sh
$ python3 -m pip install django-extensions
```

Then, in `part_django/part_django/settings.py` find the `INSTALLED_APPS` list.
Add `django_extensions` to the bottom of this section.

```py
# part_django/part_django/settings.py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'part',
    'jdango_extensions'
]

To get to a python shell, you can now run:

```
$ python3 manage.py shell_plus
```
To exit:

```
>>> quit()
```

For a nicer interface install ipython:
```
$ python3 -m pip install ipython
```

Now you can enter it:"

```
python3 manage.py shell_plus --ipython
```