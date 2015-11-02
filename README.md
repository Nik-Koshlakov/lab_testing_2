# lab_testing_2

1) pip install -r requirements.txt

2) CREATE DATABASE maps_db CHARSET utf8;

3) GRANT ALL PRIVILEGES ON maps_db.* TO maps_user IDENTIFIED BY '11';

4) python manage.py syncdb

5) python manage.py runserver
