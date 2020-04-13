# ga_django_project
Project Link: GitHub- https://github.com/grimmana/ga_django_project

# Project Description:
This application allows users to store part number information for their various possessions and is based on the tunr and nostalja and authentication documents.

Features:
- Have two related models.
- Implement Full CRUD throughout the application
- Utilizes user authentication and routes that require login for access.

Technologies used:
Django
GitHub
Python
PostgreSQL
NodeJS
Virtual environments

Issues and resolutions: foreign key error when adding an item in the form with the foreign key.

## Additional Resources

- [GA Docs: Django models](https://git.generalassemb.ly/jdr-0127/django-models)

    - [Django Docs: Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
    - [Django Docs: Models & Databases](https://docs.djangoproject.com/en/2.0/topics/db/)
    - [How to Create Django Models](https://www.digitalocean.com/community/tutorials/how-to-create-django-models)
    - [Django Docs: Migrations](https://docs.djangoproject.com/en/2.0/topics/migrations/)
    - [Django Docs: Writing Database Migrations](https://docs.djangoproject.com/en/2.0/howto/writing-migrations/)
    - [Django Docs: Admin](https://docs.djangoproject.com/en/2.1/ref/django-admin/)
    - [Django Docs: Providing initial data for models](https://docs.djangoproject.com/en/2.1/howto/initial-data/)
    - [Django Extensions](https://github.com/django-extensions/django-extensions)

- [GA Docs: Django views and templates](https://git.generalassemb.ly/jdr-0127/django-views-and-templates)




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
# part/models.py
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
# part/models.py

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
# part_django/settings.py
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
quit()
```

For a nicer interface install ipython:

```sh
$ python3 -m pip install ipython
```

Now you can enter it:"

```sh
python3 manage.py shell_plus --ipython
```

# Django Views & Templates

# View Functions

Create the Item and Item_part views in /part_jdango/part/views.py: 

```python
# part/views.py
from django.shortcuts import render
from .models import Item, Item_part

def item_list(request):
    items = Item.objects.all()
    return render(request, 'part/item_list.html', {'items': items})

def item_part_list(request):
    item_parts = Item_part.objects.all()
    return render(request, 'part/item_part_list.html', {'item_parts': item_parts})
```

# URLs

Edit /part_jdango/part_jdango/urls.py: Add to the first line import - `include` 

```python
# part_django/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('part.urls')),
]
```

Create file /part_jdango/part/urls.py that contains the app path, so that it looks like:

```python
# part/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('/item_parts', views.item_part_list, name='item_part_list')
]
```

# Templates and Django Templating Language

Create the templates that will be used to render the views.

In the directory /part_django/part/: create a `templates` directory and a `part` subdirectory.

In this path /part_django/part/templates/part/: create a new file
`item_list.html` with the following code:

```html
<!-- part/item_list.html -->
<h2>Items <a href="">(+)</a></h2>
<ul>
  {% for item in items %}
  <li>
    <a href="">{{ item.name }}</a>
  </li>
  {% endfor %}
</ul>
```

In this path /part_django/part/templates/part/: 
create  a new file
`item_part_list.html` with the following code:

```html
<h2>Item_parts</h2>
<ul>
  {% for item_part in item_parts %}
  <li>
    <a href="">{{ item_part.name }}</a>
  </li>
  {% endfor %}
</ul>
```

Ensure the server is currently running or start the server:

```
python3 manage.py runserver 8000
```
Check the following paths (listed in 
/part_django/part/urls.py) in the browser,
on the webpage you should see the lists of: 

`localhost:8000`  Items
`http://localhost:8000/item_parts/` Items_parts

# Item Detail/Show pages

Item detail
View: in the /part_django/part/views.py file, add the following code:

```python
# part/views.py
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'part/item_detail.html', {'item': item})
```

Item detail
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('items/<int:pk>', views.item_detail, name='item_detail'),
```

Item detail
TEMPLATE: in this path /part_django/part/templates/part/: 
create a new file `item_detail.html` with the following code:

```html
<!-- part/item_detail.html -->
<h2>{{ item.name }} <a href="">(edit)</a></h2>

<h3>Item_parts <a href="">(+)</a></h3>
<ul>
  {% for item_parts in item.item_parts.all %}
  <li>
    <a href="">{{ item_part.name }}</a>
  </li>
  {% endfor %}
</ul>
```

Item detail
HTML/HREF: Go back and add hrefs between the li tags in: part/templates/part/item_list.html

```html
<!-- part/item_list.html -->
<a href="{% url 'item_detail' pk=item.pk %}">
  {{ item.name }}
</a>
```

# Item_part Detail/Show pages

Item_part detail
View: in the /part_django/part/views.py file, add the following code:

```python
# part/views.py
def item_part_detail(request, pk):
    item_part = Item_part.objects.get(id=pk)
    return render(request, 'part/item_part_detail.html', {'item_part': item_part})
```

Item_part detail
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('item_parts/<int:pk>', views.item_part_detail, name='item_part_detail')
```

Item_part detail 
TEMPLATE: in this path /part_django/part/templates/part/: 
Create a new file `item_part_detail.html` with the following code:

```html
<h2>{{ item_part.name }} <a href="">(edit)</a></h2>
<h3>By: {{ item_part.item.name }}</h3>
```

Switch to: Item detail 
HTML/HREF: Go back and add hrefs between the li tags in: /part_django/part/templates/part/item_detail.html

```html
<a href="{% url 'item_part_detail' pk=item_part.pk %}">
  {{ item_part.name }}
</a>
```

Switch to: Item_part list
HTML/HREF: Go back and add hrefs between the li tags in: /part_django/part/templates/part/item_part_listl.html

```html
<a href="{% url 'item_part_detail' pk=item_part.pk %}">
  {{ item_part.name }}
</a>
```

# base.html and CSS

In this path /part_django/part/templates/part/: 
create a new file
`base.html` with the following code:

```html
<!-- part/templates/part/base.html -->
<html>
  <head>
    <title>Item</title>
  </head>
  <body>
    <h1>Item</h1>
    <nav>
      <a href="/item_parts">Item_parts</a>
      <a href="/">Items</a>
    </nav>
    {% block content %} {% endblock %}
  </body>
</html>
```

Switch to: Item list 
HTML/code: Go back and add code in: /part_django/part/templates/part/item_list.html

Each template is going to extend the base adding `{% extends 'tunr/base.html' %}` to the beginning of the file.

The content between `{% block content %}` and
`{% endblock %}` will render in place of the content block in the `base.html`
file.

```html
<!-- part/templates/part/item_list.html -->
{% extends 'part/base.html' %} {% block content %}
<h2>Items <a href="{% url 'item_create' %}">(+)</a></h2>
<ul>
  {% for item in items %}
  <li>
    <a href="{% url 'item_detail' pk=item.id %}">{{ item.name }}</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

In the directory /part_django/part/: create a `static` directory and a `css` subdirectory.

In this path /part_django/part/static/css/: create a new file `part.css` with the following code:

```css
/* part/static/css/part.css */
body {
  font-family: "Helvetica Neue", sans-serif;
  max-width: 50em;
  margin: auto;
  padding: 2em 1em;
}

nav a {
  border: 1px solid black;
  margin: 0.5em;
  padding: 0.5em;
  background-color: #eeeeee;
}

nav a:hover {
  background-color: orange;
  color: blue;
}

a,
a:visited {
  text-decoration: none;
  color: blue;
}

a:hover {
  background-color: #ccc;
}

ul {
  list-style-type: none;
}

li {
  margin: 0.25em;
}

h1 {
  font: inherit;
  color: inherit;
  letter-spacing: -0.05em;
  text-decoration: none;
  border-bottom: 1px solid black;
}

h2 > a {
  font-size: 0.75em;
}

input {
  display: block;
  margin: 5px 0 20px 0;
  padding: 9px;
  border: solid 1px black;
  width: 300px;
  background: whitesmoke;
}

input[type="submit"],
a.delete {
  width: auto;
  padding: 9px 15px;
  background-color: gray;
  border: 0;
  font-size: 14px;
  color: #ffffff;
}

a.delete {
  background-color: red;
}

.item-photo {
  width: 400px;
}

.user-info {
  float: right;
}

a.fav {
  text-decoration: none;
  color: red;
}

a.no-fav {
  text-decoration: none;
  color: black;
}

.fav:visited,
.no-fav:visited {
  text-decoration: none;
}
```

In this path /part_django/part/templates/part/: 
add the following code into `base.html`:

```html
<!-- part/templates/part/base.html -->
{% load static %}
<html>
  <head>
    <title>Item</title>
    <link rel="stylesheet" href="{% static 'css/tunr.css' %}" />
  </head>
  <body>
    <h1>Item</h1>
    <nav>
      <a href="/item_parts">Item_parts</a>
      <a href="/">Items</a>
    </nav>
    {% block content %} {% endblock %}
  </body>
</html>
```

# Item Create form

In the directory /part_django/part/: create a new file `forms.py` with the following code:


```python
# part/forms.py
from django import forms
from .models import Item, Item_part

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'ident',)
```

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
from django.shortcuts import render, redirect

from .forms import ItemForm

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'part/item_form.html', {'form': form})
```

Item_part create
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('items/new', views.items_create, name='item_create'),
```

Item form
TEMPLATE: in this path /part_django/part/templates/part/: 
create a new file `item_form.html` with the following code:

```html
<!-- part/templates/part/item_form.html -->
{% extends 'part/base.html' %} {% block content %}
<h1>New Item</h1>
<form method="POST" class="item-form">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="save btn btn-default">Save</button>
</form>
{% endblock %}
```

Item create
URL/href: in the /part_django/part/item_list.html file, add the following code on the h2 line:

```html
<!-- part/item_list.html -->
{% extends 'part/base.html' %} {% block content %}
<h2>Items <a href="{% url 'item_create' %}">(+)</a></h2>
<ul>
  {% for item in items %}
  <li>
    <a href="{% url 'item_detail' pk=item.pk %}">
      {{ item.name }}</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

# Item_part Create form

In the directory /part_django/part/: add the following code to `forms.py`:


```python
# part/forms.py
from django import forms
from .models import Item, Item_part

class Item_partForm(forms.ModelForm):

    class Meta:
        model = Item_part
        fields = ('name', 'number', 'notes',)
```

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
from django.shortcuts import render, redirect

from .forms import ItemForm, Item_partForm

def item_part_create(request):
    if request.method == 'POST':
        form = Item_partForm(request.POST)
        if form.is_valid():
            item_part = form.save()
            return redirect('item_part_detail', pk=item_part.pk)
    else:
        form = Item_partForm()
    return render(request, 'part/item_part_form.html', {'form': form})
```

Item_part create
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('item_parts/new', views.item_part_create, name='item_part_create'),
```

Item_part form
TEMPLATE: in this path /part_django/part/templates/part/: 
create a new file `item_part_form.html` with the following code:

```html
<!-- part/templates/part/item_part_form.html -->
{% extends 'part/base.html' %} {% block content %}
<h1>New Item_part</h1>
<form method="POST" class="item_part-form">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit" class="save btn btn-default">Save</button>
</form>
{% endblock %}
```

Item_part create
URL/href: in the /part_django/part/item_part_list.html file, add the following code on the h2 line:

```html
<!-- part/item_part_list.html -->
{% extends 'part/base.html' %} {% block content %}
<h2>Items_parts <a href="{% url 'item_part_create' %}">(+)</a></h2>
<ul>
  {% for item_part in items_parts %}
  <li>
    <a href="{% url 'item_part_detail' pk=item_part.pk %}">
      {{ item_part.name }}</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

Item detail
TEMPLATE: in this path /part_django/part/templates/part/: 
add the following code to h3 in `item_detail.html` :

```html
<h3>Item_parts <a href="{% url 'item_create' %}">(+)</a></h3>
```

# Item Edit form

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
def item_edit(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'part/item_form.html', {'form': form})
```

Item edit form
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('items/<int:pk>/edit', views.item_edit, name='item_edit'),
```

Item edit form
URL/href: in the /part_django/part/templates/part/item_detail.html
file, add the following code to the h2 :

```html
<!-- part/templates/part/item_detail.html -->
<h2>
  {{ item.name }} <a href="{% url 'item_edit' pk=item.pk %}">(edit)</a>
</h2>
```

# Item_part Edit form

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
def item_part_edit(request, pk):
    item_part = Item_part.objects.get(pk=pk)
    if request.method == "POST":
        form = Item_partForm(request.POST, instance=item_part)
        if form.is_valid():
            item_part = form.save()
            return redirect('item_part_detail', pk=item_part.pk)
    else:
        form = Item_partForm(instance=item_part)
    return render(request, 'part/item_part_form.html', {'form': form})
```

Item_part edit form
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('item_parts/<int:pk>/edit', views.item_part_edit, name='item_part_edit'),
```

Item_part detailedit form
URL/href: in the /part_django/part/templates/part/item_part_detail.html
file, add the following code to the h2 :

```html
<!-- part/templates/part/item_detail.html -->
<h2>
  {{ item_part.name }} <a href="{% url 'item_part_edit' pk=item_part.pk %}">(edit)</a>
</h2>
```

# Item delete form

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
def item_delete(request, pk):
    Item.objects.get(id=pk).delete()
    return redirect('item_list')
```

Item delete form
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('items/<int:pk>/delete', views.item_delete, name='item_delete'),
```

Item detail delete form
URL/href: in the /part_django/part/templates/part/item_detail.html
file, add the following code after h3 :

```python
# templates/part/item_detail.html
<div>
  <a href="{% url 'item_delete' pk=item.pk %}">DELETE</a>
</div>
```

# Item_part delete form

In this path /part_django/part: 
add the following code into `views.py`:

```python
# part/views.py
def item_part_delete(request, pk):
    Item_part.objects.get(id=pk).delete()
    return redirect('item_part_list')
```

Item_part delete form
URL: in the /part_django/part/urls.py file, add the following code:

```python
# part/urls.py
path('item_parts/<int:pk>/delete', views.item_part_delete, name='item_part_delete'),
```

Item_part detail delete form
URL/href: in the /part_django/part/templates/part/item_part_detail.html
file, add the following code after h3 :

```python
# templates/part/item_part_detail.html
<div>
  <a href="{% url 'item_part_delete' pk=item_part.pk %}">DELETE</a>
</div>
```

Ensure the server is currently running or start the server:

```
python3 manage.py runserver 8000
```
Check the following paths (listed in 
/part_django/part/urls.py) in the browser,
on the webpage you should see the lists of: 

`localhost:8000`  Items
`http://localhost:8000/item_parts/` Items_parts

Check Views