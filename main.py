"""The wiki function is defined to fetch a summary of a Wikipedia page based on a given name. 
It uses the wikipedia.summary method from the wikipedia library to retrieve the summary."""
from mylib.logic import wiki, search_wiki
"""FastAPI"""
from fastapi import FastAPI
"""Uvicorn is an ASGI web server implementation for Python"""
import uvicorn

"""The phrase function is defined to retrieve and return noun phrases from a Wikipedia page.
It uses the wiki function from the same module to fetch the Wikipedia page content. """
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
@app.get("/phrases/{name}") # The input parameter name is printed to the console.
async def phrases(name: str): # The phrase function (which you imported from mylib.logic) is called with 
    #the name parameter to extract noun phrases from the Wikipedia page.
    """Retrive Wikipedia page and return phrase"""
    print(f"Passed in name: {name}") # The result is printed to the console.
    result = phrase(name)
    print(f"Result: {result}")
    return {"result": result} # Finally, a JSON response is returned to the client with the extracted noun phrases in the "result" field.

"""This part of the code checks if the script is being executed as the main module. 
If it is, it starts the FastAPI application using the Uvicorn ASGI server. 
The application will listen on 127.0.0.1 (localhost) and port 7000."""
if __name__ == "__main__":
    uvicorn.run(app, port=7000, host="127.0.0.1")
