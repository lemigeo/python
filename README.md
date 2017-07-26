## web
#### setup sequences
1. pip install django
2. create a project
+ ex) django-admin startproject web
3. PyCharm
+ installation
+ open the project
+ create virtual environment: 
  Preperence > python interpreter > create virtual environment
4. install packages
+ ex) pip install -r ./requirements.txt
5. create an application
+ ex) ./manage.py startapp app
6. modify settings.py
+ add INSTALLED_APPS
+ change default database
7. define model classes in app/models.py
8. data migration
+ make: ./manage.py makemigrations
+ migrate: ./manage.py migrate
9. create templates directory and create index.html
