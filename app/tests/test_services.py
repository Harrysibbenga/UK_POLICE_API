from app.services import fetch_stop_and_search_data

def test_fetch_stop_and_search_data_valid(mocker):
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