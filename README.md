## Django Starter Project

Create Virtual Environment

- if windows

    ```bash
    python -m venv .venv
    ```

- if mac or linux

    ```bash
    python3 -m venv .venv
    ```

Activate Virtual Environment

- if windows

    ```bash
    source .venv/Scripts/activate
    ```


- if mac or linux

    ```bash
    source .venv/bin/activate
    ```

- if you want to deactivate

    ```bash
    deactivate
    ```

Install Django
    
```bash 
pip install django
```

Create Django Project

```bash
django-admin startproject <project_name>
```

Run Django Project

```bash
python manage.py runserver
```

Setup pylint

- install pylint

    ```bash
    pip install pylint
    ```

- install pylint-django plugin

    ```bash
    pip install pylint-django
    ```

- create .pylintrc file

    ```bash
    pylint --generate-rcfile > .pylintrc
    ```

- add this to .pylintrc file

    ```bash
    [MASTER]
    load-plugins=pylint_django
    ```
[]: #     ```
