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

7. Setup DRF(Django Rest Framework)

- Install DRF package

  ```sh
  pip install djangorestframework
  ```

- Add installed DRF package to requirements file

  ```sh
  pip freeze | grep djangorestframework >> requirements.txt
  ```

- Install DRF app in project setting

  ```python
  INSTALLED_APPS = [
    ...,
    'rest_framework',
  ]
  ```

8. Setup Test Coverage

- Install Coverage package

  ```sh
  pip install coverage
  ```

- Add installed Coverage package to requirements file

  ```sh
  pip freeze | grep coverage >> requirements.txt
  ```

- Run tests with coverage

  ```sh
  coverage run manage.py test
  ```

- See coverage report on terminal

  ```sh
  coverage report
  ```

- Generate HTML report

  ```sh
  coverage html
  ```

9. Setup MyPy

- Install MyPy package

  ```sh
  pip install mypy
  ```

- Add installed mypy package to requirements file

  ```sh
  pip freeze | grep mypy== >> requirements.txt
  ```

- Install django stubs package

  ```sh
  pip install django-stubs
  ```

- Add installed django stubs package to requirements file

  ```sh
  pip freeze | grep django-stubs== >> requirements.txt
  ```

- Install drf stubs package

  ```sh
  pip install djangorestframework-stubs
  ```

- Add installed drf stubs package to requirements file

  ```sh
  pip freeze | grep djangorestframework-stubs >> requirements.txt
  ```

- Add MyPy config file `mypy.init`

  ```init
  [mypy]
  plugins = mypy_django_plugin.main
  exclude = migrations|tests

  [mypy.plugins.django-stubs]
  django_settings_module = "<inner-porject-name>.settings"
  ```

- Note:- config file [doc](https://mypy.readthedocs.io/en/latest/config_file.html)

- Run mypy type checking

  ```sh
  mypy .
  ```

10. Setup black

- Install black package

  ```sh
  pip install black
  ```

- Add installed black package to requirements file

  ```sh
  pip freeze | grep black >> requirements.txt
  ```

- Add black config in `puproject.toml` file

  ```toml
  [tool.black]
  force-exclude = "/migrations/"
  ```

- Note:- black official [doc](https://black.readthedocs.io/en/stable/getting_started.html)

- Install VS Code Black extension [`ms-python.black-formatter`](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

- Configure VS Code python default formatter to black in `.vscode/settings.json` file

  ```json
  {
    "[python]": {
      "editor.defaultFormatter": "ms-python.black-formatter"
    }
  }
  ```

- Fix formatting using black

  ```sh
  black .
  ```

11. Setup isort

- Install isort package

  ```sh
  pip install isort
  ```

- Add installed isort package to requirements file

  ```sh
  pip freeze | grep isort >> requirements.txt
  ```

- Add MyPy config file `isort.cfg`

  ```cfg
  [settings]
  profile = black
  verbose = true
  skip_glob = **/migrations/*.py
  ```

- Install VS Code Black extension [`ms-python.isort`](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)

- Configure VS Code to organize python imports using isort in `.vscode/settings.json`

  ```json
  {
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    },
    "isort.args": ["--profile", "black", "--skip-glob", "*/migrations/*"]
  }
  ```

- Sort imports using isort

  ```sh
  isort .
  ```
