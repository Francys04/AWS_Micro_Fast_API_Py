# Wikipedia API using FastAPI

This project implements a FastAPI-based API for interacting with Wikipedia data and provides additional functionalities.

## Running the FastAPI Application

1. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt


## Run the FastAPI application:
```
uvicorn main:app --host 0.0.0.0 --port 7000
```
- Access the API at: 
```
http://127.0.0.1:7000/
```

## API Endpoints
- /: Get a simple status message.
- /search/{value}: Search Wikipedia based on a query value.
- /wiki/{name}: Retrieve Wikipedia page by name.
- /phrases/{name}: Retrieve Wikipedia page and return phrases.
## Makefile Commands
- make install: Install project dependencies.
- make format: Format the code using black.
- make lint: Run lint checks using pylint.
- make test: Run tests using pytest and generate coverage reports.
- make build: Build a Docker container for the application.
- make run: Run the Docker container.
## Testing
- Test cases are available in test_main.py and test_logic.py.

## Install test dependencies:

`pip install --upgrade pip`
`pip install -r test_requirements.txt`
## Run tests:
`pytest test_main.py
pytest test_logic.py`

## Additional Information
- The application uses the fastapi and uvicorn libraries to create a web API.
- The wikipedia library is used for fetching Wikipedia data.
- The textblob library is used for natural language processing (NLP) tasks.


## Functionality
1. Create virtual enviroment
2. Create emty files: Makefile, requiremeents.txt, main.py, Dockerfile, mylib/__init__.py and logic.py
3. Populate "Makefile"
4. Setup continious Integretion, i.e. check code for issues like lint errors
5. Build cli using python fire library './cli-fire.py' to test logic 