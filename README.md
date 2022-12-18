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

Setup Pylint

- Reference Links
    
        - [pylint](https://github.com/PyCQA/pylint/)
    
        - [pylint-django](https://github.com/PyCQA/pylint-django/)

        - Blog: [How to setup pylint for django project](https://dkolodzey.medium.com/pylint-django-with-github-actions-2e3ef05dd34a)


- Install pylint

    ```bash
    pip install pylint
    ```

- Install pylint-django pylint plugin

    ```bash
    pip install pylint-django
    ```

- Create pylint config file if you want to customize

    ```bash
    pylint --generate-rcfile > .pylintrc
    ```

- Add pylint_django in load-plugins to pylint config file

    ```text
    [MASTER]
    load-plugins=pylint_django
    ```

- Add django settings module in pylint config file

    ```text
    [pylint-django]
    django-settings-module=<project_name>.settings
    ```

- Run pylint

    ```bash
    pylint **/*.py
    ```

- NOTE: if you not want to create pylint config file, you can run pylint with 

```bash
pylint --load-plugins=pylint_django --django-settings-module=<project_name>.settings **/*.py
```

- If you are using vscode, you can install pylint extension and it will automatically run pylint on save. for that you need to add this in settings.json

    ```json
    {
        {
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "python.linting.pylintArgs": [
            "--load-plugins",
            "pylint_django",
            "--django-settings-module=<project_name>.settings"
        ]
    }
    ```

    [Setup Reference Links](https://dkolodzey.medium.com/pylint-for-django-in-vscode-f3fadb8462d)