# log-rock-challenger
Goal: Build a REST API for managing insurance policies.

## Installation and configuration

This project was developed using [Python 3.13](https://www.python.org/downloads/)

### Clone repository

```
git clone https://github.com/BatistaYuri/log-rock-challenger.git
```

### Install dependencies

```
pip install django djangorestframework
```

### Configure database

```
python manage.py makemigrations
python manage.py migrate
```

## Execution
### Run application

```
python manage.py runserver
```

### Features
Create a new policy and retrieve a list of all policies:

```
http://127.0.0.1:8000/api/policies
```
Retrieve details of a specific policy, update an existing policy and delete a policy:

```
http://127.0.0.1:8000/api/policies/${policy_id}
```

### Test

```
python manage.py test
```