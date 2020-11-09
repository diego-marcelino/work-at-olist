ENV=.local

init_dev_env:
	pip install -r requirements/local.txt
	pre-commit install
	pre-commit autoupdate

start_local_db:
	docker-compose -f local-db.yml up --detach

stop_local_db:
	docker-compose -f local-db.yml down

run_local:
	python merge_dotenvs.py $(ENV)
	python manage.py migrate
	python manage.py runserver_plus

run_tests:
	coverage run -m pytest
	coverage report
