## Django Starter Project

1. Create Virtual Environment

- if windows

  ```bash
  python -m venv .venv
  ```

- if mac or linux

  ```bash
  python3 -m venv .venv
  ```

2. Activate Virtual Environment

- if windows

  ```bash
  source .venv/Scripts/activate
  ```

- if mac or linux

  ```bash
  source .venv/bin/activate
  ```

- Note:- if you want to deactivate

  ```bash
  deactivate
  ```

3. Setup Django project

- Install Django package

  ```sh
  pip install Django
  ```

- Add installed Django package to requirements file

  ```sh
  pip freeze | grep Django > requirements.txt
  ```

- Start Django project

  ```sh
  django-admin startproject <project-name> .
  ```

4. Setup Django app

- Start Django app 

  ```sh
  python3 manage.py startapp <app-name>
  ```

- Install Django app in project setting

  ```python
  INSTALLED_APPS = [
    ...,
    '<app-name>',
  ]
  ```

5. Setup Django Model

- Generate migration file for model

  ```sh
  python3 manage.py makemigrations
  ```

- Apply migration

  ```sh
  python3 manage.py migrate
  ```

6. Run unit tests

  ```sh
  python3 manage.py test
  ```