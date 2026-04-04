# otc-backend

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

3. Install dependencies

- using pip

  ```bash
  pip install .[dev]
  ```

- using uv

  ```bash
  uv sync --group dev
  ```

4. Apply database migrations

  ```sh
  python3 manage.py migrate
  ```

5. Run unit tests

```sh
python3 manage.py test
```

6. Test Coverage

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

7. Setup MyPy

- Note:- config file [doc](https://mypy.readthedocs.io/en/latest/config_file.html)

- Run mypy type checking

  ```sh
  mypy .
  ```

8. Setup black

- Note:- black official [doc](https://black.readthedocs.io/en/stable/getting_started.html)

- Install VS Code Black extension [`ms-python.black-formatter`](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

- Fix formatting using black

  ```sh
  black .
  ```

9. Setup isort

- Install VS Code isort extension [`ms-python.isort`](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)

- Sort imports using isort

  ```sh
  isort .
  ```

10. Setup pylint

- Install VS Code pylint extension [`ms-python.pylint`](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

- Run pylint for code quality checks

  ```sh
  pylint **/*.py
  ```

11. Setup pre commit

- Install pre commit dependencies

  ```sh
  pre-commit install
  ```

- Run pre-commit hooks manually

  ```sh
  pre-commit run --all-files
  ```

- Note:- pre commit official [doc](https://pre-commit.com/)

12. Setup pre push hook

- for linux or macos

  ```sh
  cp .githooks/pre-push .git/hooks/pre-push && chmod +x .git/hooks/pre-push
  ```

- for windowns

  ```sh
  copy .githooks\pre-push .git\hooks\pre-push
  ```

13. Setup VS Code test runner

- Add manage.py path variable in `.env` file

  ```env
  MANAGE_PY_PATH=manage.py
  ```

14. Install recommended VS Code extensions

- Open the extensions sidebar in VS Code `ctrl+shift+x` or `cmd+shift+x`

- Type @recommended in the search bar

- Install the recommended extensions

15. Generate OpenAPI Schema

  ```sh
  python manage.py spectacular --color --file schema.yml
  ```

16. Generate secret key

  ```sh
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
