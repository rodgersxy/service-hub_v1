![WhatsApp Image 2023-11-10 at 01 22 36](https://github.com/rodgersxy/service-hub_v1/assets/47353893/d087d151-cc91-4455-a13c-d86f0fe61187)

![WhatsApp Image 2023-11-10 at 01 26 57](https://github.com/rodgersxy/service-hub_v1/assets/47353893/6df3ba5e-0938-4190-a6ea-08f4cca6a3d2)

![WhatsApp Image 2023-11-10 at 01 25 18](https://github.com/rodgersxy/service-hub_v1/assets/47353893/e9d36d47-5e0a-4b43-933e-6d7a1f9771ae)




# SERVICE HUB

## TABLE OF CONTENTS
* Introduction
* Inspirational Story
* Authors
* Tech Stack
* Database Section
* Acknowledgements

## INTRODUCTION
* In a world increasingly dominated by digital platforms, the realm of hand-skilled professionals often finds itself overlooked. Enter ServiceHub, a revolutionary web application designed to connect skilled individuals with broadclient network, addressing the void left by platforms favouring soft skills in the digital age.

* ServiceHub aims to brigde the gap between skilled workers and potential clients, ensuring convenience and accesibility for both parties.

## Authors
```
Benedict - Mastermind behind the backend magic. Delved deep into the complexities of server-side development. His exepertise in database management and server operations was instrumental in bringing the technical backbone of ServiceHub to life.

Koki - A coding virtuoso with an eye for design. Koki played a pivotal role in crafting the user interface and user exeperience of servicehub.

Rodgers - Took role of Project lead. He oversaw the project's development, ensuring smooth collaboration, and diving into the intricacies of backend development.
```


## TECH STACK
* Python - The Backend Language
* Tailwind-Css - The Frontend language
* MySQL - Relational Database Management System
* Django - Web Framework


## DATABASE SECTION
* In the **settings.py** file of the django framework, you'll notice that the default database is *sqlite* which is not fit to use on production level.
* This is the default of settings.py Database section:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

* Luckily with django we can integrate it with other database servers i.e: **PostgreSQL, MariaDB, MySQL and Oracle**
* For this project we chose to work with **MySQL** as our backend database.
* With MySQL, there are a numbers of steps to follow to connect your django project to it. Here they are:

1.Installation of MySQL
```
-sudo apt-get install mysql-server libmysqlclient-dev
-pip install mysqlclient (Run this command in the virtual environment of your current django project.This package enables MySQL connect to the django project)
-sudo apt-get install pkg-config
```

* Restart the MySQL server with:
```
sudo service mysql restart
```

* Check status of MySQL:
```
sudo service mysql status
```


2.Create a MySQL Database
* Login into your SQL
```
mysql -u root -p
```
* After login, run:
```
CREATE DATABASE your_database_name;
```
* Replace your_database_user and your_database_name with your actual MySQL username and desired database name.


3.Configure Django settings(The Database section)
* Open your Django project's settings.py file and locate the DATABASES configuration. Update the ENGINE, NAME, USER, and PASSWORD settings to connect to your MySQL database. Modify the HOST and PORT if needed.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Change to the MySQL server address if it's not on your local machine
        'PORT': '3306',  # Default MySQL port
    }
}
```

4.Run Migrations
* After updating your database settings, run the following Django management command to apply migrations:
```
python manage.py migrate
```

5.Test the connection
* Run the development server and check if your Django project connects to the MySQL database without errors:
```
python manage.py runserver
```
* Visit http://127.0.0.1:8000/ in your browser and verify that your application is working with the MySQL database.


## ACKNOWLEDGEMENTS
* Holberton School
* ALX Software Engineering(Mentors & Students)
* Team Members and Reviewers.
