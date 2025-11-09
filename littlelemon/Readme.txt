====== Admin ======
username: admin
password: littlelemon!


====== API Path ======
/restaurant/menu/ (need authentication)
/restaurant/booking/tables/
/restaurant/

====== Set Up ======
pipenv shell
pipenv install django
pipenv install mysqlclient

**You might need to install these to connect to MySQL successfully using mysqlclient:
pipenv install pymysql
pipenv install cryptography


====== Connect to MySQL Database ======
mysql -u root -p
Enter password: <your root password>
mysql> CREATE DATABASE reservations;
mysql> SHOW DATABASES;
mysql> CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employ@123!';
mysql> GRANT ALL ON *.* TO 'admindjango'@'localhost';


====== Run Project ======
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


====== Check Data in Database ======
mysql> USE littlelemon;
mysql> SHOW TABLES;
mysql> SELECT * FROM restaurant_booking;


====== Unit Test ======
project level:
python manage.py test


====== Registration and Authentication ======
1. POST http://127.0.0.1:8000/auth/users/
body:
{
    "username": "testuser",
    "password": "testpassword",
    "re_password": "testpassword"
}

2. POST http://127.0.0.1:8000/auth/token/login/
body
{
    "username": "testuser",
    "password": "testpassword"
}

3. Receive Token