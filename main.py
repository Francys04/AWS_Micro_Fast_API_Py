from mylib.logic import wiki, search_wiki

# FastAPI
from fastapi import FastAPI

# Uvicorn is an ASGI web server implementation for Python
import uvicorn

# nlp phrases
from mylib.logic import phrase


# create Fast api
app = FastAPI()


# result = logic
# print(result)


# verify message of api
@app.get("/")
async def root():
    return {"message": "Wikipedia API"}


# get post of search value(str) data from wikipedia
@app.get("/search/{value}")
async def search(value: str):
    """Page to search wikipedia"""
    result = search_wiki(value)
    return {"result": result}


# get data by search full name
@app.get("/wiki/{name}")
async def searchin(name: str):
    """Retrive Wikipedia page"""
    result = wiki(name)
    return {"result": result}


# get phrase
@app.get("/phrases/{name}")
async def phrases(name: str):
    """Retrive Wikipedia page and return phrase"""
    print(f"Passed in name: {name}")
    result = phrase(name)
    print(f"Result: {result}")
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=7000, host="127.0.0.1")
