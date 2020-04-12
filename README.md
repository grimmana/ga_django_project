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
$ django-admin startapp tunr
```

Application structure should look like this?
 
- .env
- .vscode
- part
- part_django





