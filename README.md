# Django_EmployeeInfo_todoapp_using_mysql
To Do list app with User Registration, Login and full Create Read Update and DELETE functionality.

In this App we will:

1. Create basic User Register view using generic User Creation Form and Form view with user authentication
2. Create User Login view with confirmation Username and Password
3. Create Employee Info CRUD app
4. Add new Employee using generic Create View
5. Update Employee Info using generic Update View
6. Delete Employee using generic Delete View
7. View Employee List for Specific User

## Django Project Setup
 pip install -r requirements.txt

1. django-admin startproject todo_application
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py createsuperuser

### Just Run this command for server deployment:
  python manage.py runserver

### Database Configuartion with Django:
Install MySQL Database using this link: https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database

## Create Django app:
### Run this command: 
   python manage.py startapp todo_app
   
Include app in project settings:

...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo_app',
]


We will start with the basic sign up features that django provides by default.

## Registration Form
we have been using the default fields that UserCreationForm provides us. But what if we wanted the email address of the new user which is 
the important part aside from the username and password.For that we can inherit a new form class from UserCreationForm.

Also use the <b> crispy_form bootstrap4 </b> api that helps to manage Django forms. It allows adjusting forms' properties (such as method, send button or CSS classes) on the backend without having to re-write them in the template.

## Login Form
we have been using the default fields that Login View provides us. That authenticate the user with password.

## Employee Info CRUD app
For this we have been using django generic class-based-views.
1. The class <b>EmployeeList</b> takes <b>List View</b> that inherits directly from 1 view and 1 mixin to give this view all the attributes and methods that it has.
2. The class <b>EmployeeDetail</b> takes <b>DetailView</b> inherits directly from 1 view and 1 mixin, that give the detail view of an Employee that it has.
3. The class <b>EmployeeCreate</b> takes <b>CreateView</b> inherits directly from 1 view and 1 mixin, that create/add view of an employee.
4. The class <b>EmployeeUpdate</b> takes <b>UpdateView</b> inherits directly from 1 view and 1 mixin. This view by default follows the same template_naming convention and form principles as the create view and Update the employee infro.
5. The class <b>DeleteView</b> takes <b>DeleteView</b> inherits directly from 1 view and 1 mixin, that delete the view of an employee.
