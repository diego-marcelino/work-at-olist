# Work at Olist

[![django ci](https://github.com/diego-marcelino/work-at-olist/workflows/CI/badge.svg)](https://github.com/diego-marcelino/work-at-olist/actions)
[![codecov](https://codecov.io/gh/diego-marcelino/work-at-olist/branch/master/graph/badge.svg)](https://codecov.io/gh/diego-marcelino/work-at-olist)
[![cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
[![yapf](https://img.shields.io/badge/code%20style-YAPF-000000.svg)](https://github.com/google/yapf)
[![Heroku](https://img.shields.io/badge/deploy-Heroku-6567A5.svg)](https://damworkatolist.herokuapp.com/)



## Development guide (Linux)

> This project has been develped and testes on Linux operating system and there is no garantee it works properly on other operating system.


1. Create and activate Python virtual environment. This may be done by many ways, a siple one is by using _virtualenv_.

```shell
pip install virtualenv
virtualenv -p python3.8 venv
source venv/bin/activate
```

2. Init environment for development, install python dependencies and pre commit hooks for code linting.

```shell
make init_dev_env
```

3. Start local database.

3.1. Local database with Docker. There is a Docker Compose file for local database, which may be started using command:

```shell
make start_local_db
```

For stop this database execution use command:

```shell
make stop_local_db
```

This Compose file has also a PgAdmin accessible on localhost:9000. Use credentials defined on local env files (_.envs/.local/_).

3.2. Custom database. For other database copy the folder _.envs/.local/_ and set access and credential settings.

4. Create superuser for access admin area. Use the following command:

```shell
python manage.py createsuperuser
```

5. Run tests using command:

```shell
make run_tests
```

6. Run code lint:

```shell
pre-commit run -a
```

7. Run application:

```shell
make run_local .local
```

If defined custom env files for other database use as parameter:

```shell
make run_local .my_custom_env_dir
```
