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

3. Setup Django project with app

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
