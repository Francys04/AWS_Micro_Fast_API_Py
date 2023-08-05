from main import app
"""import fastapi -> create web APIs easily. """
from fastapi import FastAPI
"""The TestClient is used to simulate HTTP requests to your FastAPI application for testing purposes."""
from fastapi.testclient import TestClient

# This client will be used to send requests to the FastAPI application during testing.
client = TestClient(app)

# Test if status code and json output will hame same result
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API"}
    # This line asserts that the JSON content of the response is equal to {"message": "Wikipedia API"}, 
    # which checks if the response content matches the expected result.

# Test phrases/Barack Obama
# The second test function, test_read_phrase(), is similar and follows the same pattern. It 
# tests the "/phrases/Barack Obama" endpoint and checks whether the response status code and JSON content match the expected values.
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