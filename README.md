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

- Install pylint for code analysis and linting

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

<!-- - Or use [google style guide](https://google.github.io/styleguide/pyguide.html)

    [pylintrc file](https://google.github.io/styleguide/pylintrc) -->

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

TODO - Fix this is not working

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

Setup Black for code formatting

- Reference Links

        - [black](https://black.readthedocs.io/en/stable/)
        - [Blog Link](https://ctrlzblog.com/how-to-set-up-black-to-automatically-format-your-django-project/)

- Install black

  ```bash
  pip install black
  ```

- Run black

  ```bash
  black .
  ```

- Check black formatting

  ```bash
  black --check .
  ```

- If you are using vscode

  - Install VS Code Extension `ms-python.black-formatter`

  - add this in settings.json
    ```json
    {
      "editor.formatOnSave": true,
      "python.formatting.provider": "black"
    }
    ```

Setup mypy for static type checking

- Reference Links

        - [mypy](https://mypy.readthedocs.io/en/stable/)
        - [django-stubs github repo](https://github.com/typeddjango/django-stubs)

- Install mypy

        ```bash
        pip install mypy
        ```

- Install django-stubs for django type checking

        ```bash
        pip install django-stubs
        ```

- Note this is not required in current case, but if you are using django models, you need to install django-stubs

  - [mypy config docs](https://mypy.readthedocs.io/en/latest/config_file.html)
  - [Stack Overflow Reference](https://stackoverflow.com/questions/59031982/type-annotations-for-django-models)

  - Add django-stubs in plugins in mypy config file `mypy.ini`

    ```text
    [mypy]
    plugins = mypy_django_plugin.main
    ```

  - Add django settings module in mypy config file `mypy.ini`
    ```text
    [mypy.plugins.django-stubs]
    django_settings_module = <project_name>.settings
    ```

- Run mypy

  ```bash
  mypy .

  ```

- If you are using vscode, you need to add this in settings.json

  ```json
  {
    "python.linting.mypyEnabled": true,
    "python.linting.mypyArgs": ["--strict"]
  }
  ```

- [Reference Blog](https://dev.to/jodaut/python-type-checking-with-visual-studio-code-46a7)

Setup isort for sorting imports

- Reference Links

  - [isort](https://pycqa.github.io/isort/)
  - [github wiki](https://github.com/PyCQA/isort/wiki/isort-Settings)

- Install isort

  ```bash
  pip install isort
  ```

- Run isort

  ```bash
  isort .
  ```

- Check isort

  ```bash
  isort --check .
  ```

- If want to customize isort, you can create isort config file `isort.cfg`

  ```text
  [settings]
  verbose = true
  skip_glob = **/migrations/*.py
  ```

- NOTE: supported options are [here](https://pycqa.github.io/isort/docs/configuration/options.html)

- If you are using vscode, you need to add this in settings.json

  ```json
  {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    },
    "isort.args": ["skip_glob", "*/migrations/*"]
  }
  ```
