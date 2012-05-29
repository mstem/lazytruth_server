rm dev-db.sql
python manage.py syncdb
rm apps/data/migrations/0001_initial.*
python manage.py schemamigration data --initial
python manage.py migrate
python manage.py loadmattdata
