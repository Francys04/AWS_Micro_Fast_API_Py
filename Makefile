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
	python -m pytest -vv --cov=mylib test_logic.py
build:
# build container
deploy:
# deploy
all: install lint test deploy