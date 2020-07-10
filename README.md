# Blog
Blog is w website that can user , loging , read article that that published
from admin use and also the user can like this article

Blog also have a list of API's

# Requirments
1. Python 3: https://www.python.org/downloads/
2. Postgres DB: https://www.postgresql.org/download/
3. PgAdmin: https://www.pgadmin.org/download/
4. Nodejs: https://nodejs.org/en/

# Getting Started
1. Clone the project: https://github.com/Hamza-abughazaleh/Blog.git
2. Create python enviroment:
   - Open Terminal
   - sudo apt install virtualenv
   - virtualenv "env name" --python=/usr/bin/python3
3. Activate Your enviroment:
   - Open Terminal
   - source "env name"/bin/activate
4. Go to project directory and install requirements file by terminal: pip install -r requirements.txt
5. Create your DB from pgadmin
6. Go to settings.py and edit this code:
    ``` 
    DATABASES = {
    	'default': {
       		'ENGINE': 'django.db.backends.postgresql_psycopg2',
       		'NAME': '***', #add your db name you created
       		'USER': '***', #add your db authentication
       		'PASSWORD': '***',
       		'HOST': '127.0.0.1',
       		'PORT': '5432',
    		}
   	}

7. Go to project directory and run:
    - npm install
  
8. Go to project directory and do this commands by terminal: 
   - python manage.py migrate
   - python manage.py createsuperuser #to create super user (admin)
   - python manage.py runserver

9. Go to 127.0.0.1:8000/en/

# API's url
1. 127.0.0.1:8000/en/user/api-v1
2. 127.0.0.1:8000/en/main/api-v1

# What's included
1. Django 3.0.8: https://docs.djangoproject.com/en/3.0/
2. Django Rest Framework 3.11.0: https://www.django-rest-framework.org/

