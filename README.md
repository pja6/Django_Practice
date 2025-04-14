# Django_Practice
Learning to use Django

## Notes

### step 1:

Install Django

    pip install django

### Step 2:

Set up project file

    django-admin startproject myproject

(Optional) Activate virtual environment
    python3 -m venv venv

    source venv/bin/activate
Your terminal prompt should now show (venv) at the beginning

for w/e reason Django mysqlclient doesn't work so use

pip install pymysql

### Step 3:

Initialize app

    python manage.py startapp [appname]

### Step 4.
Install REST Framework

        pip install djangorestframework

### Step 5.
Update requirements

        pip freeze > requirements.txt

#### Note:
Can recreate environment using

        pip install -r requirements.txt


