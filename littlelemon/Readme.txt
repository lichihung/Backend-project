====== Admin ======
username: admin
password: littlelemon!


====== Path ======
/restaurant/
/restaurant/menu/     (need authentication)
/restaurant/booking/tables/


====== Create a Menu Item ======
1. Go to Insomnia
2. POST http://127.0.0.1:8000/restaurant/menu
{
  "title": "Margherita Pizza",
  "price": 12.5,
  "stock": 20
}


====== Unit Test ======
(project level)
python manage.py test


====== Registration and Authentication ======
1. Go to Insomnia
2. POST http://127.0.0.1:8000/auth/users/
Body:
{
    "username": "testuser",
    "password": "testpassword",
    "re_password": "testpassword"
}
3. POST http://127.0.0.1:8000/auth/token/login/
Body
{
    "username": "testuser",
    "password": "testpassword"
}
4. Receive Token


====== Set Up ======
pipenv shell
pipenv install django
pipenv install mysqlclient

**You might need to install these to connect to MySQL successfully using mysqlclient:
pipenv install pymysql
pipenv install cryptography


====== Run Project ======
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


====== Connect to MySQL Database ======
mysql -u root -p
Enter password: <your root password>
mysql> CREATE DATABASE littlelemon;
mysql> SHOW DATABASES;
mysql> CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employ@123!';
mysql> GRANT ALL ON *.* TO 'admindjango'@'localhost';


====== Check Data in Database ======
mysql> USE littlelemon;
mysql> SHOW TABLES;
mysql> SELECT * FROM restaurant_menuitem;