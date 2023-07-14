from main import app
# import fastapi 
from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)

# test if status code and json output will hame same result
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API"}

# test phrases/Barack Obama
def test_read_phrase():
    response = client.get("/phrases/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result":
            ["barack hussein obama ii",
             "bə-rahk hoo-sayn oh-bah-mə",
             "august",
             "american politician",
             "44th president"]
            }