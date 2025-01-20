import pytest
from app import create_app
from app.services import fetch_stop_and_search_data

@pytest.fixture
def client():
    """
        Creates a test client for the Flask application.

        This function initializes the Flask application in testing mode and 
        provides a test client that can be used to simulate HTTP requests 
        to the application.

        Yields:
            FlaskClient: A test client for the Flask application.
    """
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_missing_parameters(client):
    """
        Test the /stop-and-search/outcome endpoint with missing parameters.
        
        This test sends a GET request to the /stop-and-search/outcome endpoint without
        the required 'force' and 'date' parameters and asserts that the response status
        code is 400 (Bad Request). It also checks that the error message in the response
        contains the expected text indicating that both 'force' and 'date' parameters
        are required.
        
        Args:
            client: The test client used to make requests to the application.
        Asserts:
            - The response status code is 400.
            - The error message in the response contains the text "Both 'force' and 'date'".
    """
    
    response = client.get("/stop-and-search/outcome")
    assert response.status_code == 400
    assert "Both 'force' and 'date'" in response.json["error"]

def test_invalid_date(client):
    """
        Test the endpoint for handling invalid date formats.
        
        This test sends a GET request to the `/stop-and-search/outcome` endpoint with an invalid date format.
        It asserts that the response status code is 400 (Bad Request) and that the response contains an error message indicating an invalid date format.
        
        Args:
            client (FlaskClient): The test client used to make requests to the application.
            
        Asserts:
            response.status_code (int): The HTTP status code of the response should be 400.
            response.json["error"] (str): The error message in the response should indicate an invalid date format.
    """
    
    response = client.get("/stop-and-search/outcome?force=metropolitan&date=2022-13")
    assert response.status_code == 400
    assert "Invalid date format" in response.json["error"]

def test_valid_request(mocker, client):
    """
        Test the /stop-and-search/outcome endpoint with a valid request.
        
        This test mocks the fetch_stop_and_search_data function to return predefined data
        and then calls the endpoint to verify that the response is as expected.
        
        Args:
            mocker: The pytest-mock fixture used to mock dependencies.
            client: The test client used to make requests to the application.
            
        Assertions:
            - The response status code should be 200.
            - The response JSON should contain the correct total value.
            - The response JSON should contain the correct breakdown values for "Arrest" and "A no further action disposal".
    """
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
    
def test_rate_limit(client):
    for _ in range(5):
        response = client.get("/stop-and-search/outcome?force=metropolitan&date=2022-08")
        assert response.status_code != 429

    response = client.get("/stop-and-search/outcome?force=metropolitan&date=2022-08")
    assert response.status_code == 429
