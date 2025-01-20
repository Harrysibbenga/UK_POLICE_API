from app.services import fetch_stop_and_search_data

def test_fetch_stop_and_search_data_valid(mocker):
    """
        Test the fetch_stop_and_search_data function with valid data.
        
        This test uses the mocker fixture to patch the requests.get method, simulating
        a successful API response with predefined mock data. The mock data contains
        four stop and search records with different outcomes.
        
        The test verifies that the fetch_stop_and_search_data function correctly
        processes the mock data and returns the expected result, which includes the
        total number of records and a breakdown of outcomes.
        
        Args:
            mocker (pytest_mock.plugin.MockerFixture): The mocker fixture used to
            patch the requests.get method.
            
        Asserts:
            The total number of records is 4.
            The number of "Arrest" outcomes is 3.
            The number of "A no further action disposal" outcomes is 1.
    """
    
    mock_data = [
        {"outcome": "Arrest"},
        {"outcome": "Arrest"},
        {"outcome": "A no further action disposal"},
        {"outcome": "Arrest"}
    ]
    mocker.patch("requests.get", return_value=mocker.Mock(json=lambda: mock_data, status_code=200))
    
    result = fetch_stop_and_search_data("metropolitan", "2022-08")
    print(result)
    assert result["total"] == 4
    assert result["breakdown"]["Arrest"] == 3
    assert result["breakdown"]["A no further action disposal"] == 1