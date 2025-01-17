import pytest
from app import create_app
from app.services import fetch_stop_and_search_data

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_missing_parameters(client):
    response = client.get("/stop-and-search/outcome")
    assert response.status_code == 400
    assert "Both 'force' and 'date'" in response.json["error"]

def test_invalid_date(client):
    response = client.get("/stop-and-search/outcome?force=metropolitan&date=2022-13")
    assert response.status_code == 400
    assert "Invalid date format" in response.json["error"]

def test_valid_request(mocker, client):
    # Mock the fetch_stop_and_search_data function
    mock_data = {"total": 8, "breakdown": {"Arrest": 5, "A no further action disposal": 3}}
    mocker.patch("app.routes.fetch_stop_and_search_data", return_value=mock_data)
    
    # Call the route endpoint
    response = client.get("/stop-and-search/outcome?force=metropolitan&date=2022-08")
    
    # Assertions
    assert response.status_code == 200
    assert response.json["total"] == 8
    assert response.json["breakdown"]["Arrest"] == 5
    assert response.json["breakdown"]["A no further action disposal"] == 3
