run:
	flask run --debug
migrate:
	flask db migrate
upgrade:
	flask db upgrade
init:
	flask db init
add-req:
	pip freeze > requirements.txt
install-req:
	pip install -r requirements.txt