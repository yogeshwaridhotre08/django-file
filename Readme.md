# Django To-Do List Application

This is a simple Django application that allows users to manage their to-do lists.

## Installation

##  Create a virtual environment (optional but recommended)

python -m venv env

## Activate the virtual environment
### On Windows:

.\env\Scripts\activate


### On macOS/Linux:


source env/bin/activate

##  Install dependencies

pip install -r requirements.txt

## Database Setup

### Apply migrations

python manage.py migrate

### Create a superuser (optional)

python manage.py createsuperuser


## Run the Application

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.


### Usage

Visit the registration page to create a new account.
Log in using your credentials.
Manage your to-do list by adding, editing, and deleting tasks.