install:
# install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt
format:
# format -> The format of a Makefile is based on rules and targets
	black *.py mylib/*.py
lint:
# flake8 or pylint ->to have some static checks that tell us if we have bad code quality
	pylint --disable=R,C *.py mylib/*.py
test:
# test
	python -m pytest -vv --cov=mylib test_main.py
	python -m pytest -vv --cov=mylib test_logic.py
build:
# build container
	docker build -t deploy-fatsapi .
run:
# run docker, image id from docker desktop, refresh after make build
	docker run -p 127.0.0.1:7000:7000 0a0b4819c62b
deploy:
# deploy
all: install lint test deploy