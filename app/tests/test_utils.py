from app.utils import validate_date

def test_validate_date_valid():
    assert validate_date("2022-08") == True

def test_validate_date_invalid():
    assert validate_date("2022-13") == False

def test_validate_date_empty():
    assert validate_date("") == False