from app.utils import validate_date

def test_validate_date_valid():
    """
        Test case for validate_date function with an valid date string.

        This test checks if the validate_date function correctly identifies
        an valid date string ("2022-08") and returns True.

        Expected result: True
    """
    
    assert validate_date("2022-08") == True

def test_validate_date_invalid():
    """
        Test case for validate_date function with an invalid date string.

        This test checks if the validate_date function correctly identifies
        an invalid date string ("2022-13") and returns False.

        Expected result: False
    """
    
    assert validate_date("2022-13") == False

def test_validate_date_empty():
    """
        Test case for validate_date function with an empty date string.

        This test checks if the validate_date function correctly identifies
        an empty date string ("") and returns False.

        Expected result: False
    """
    
    assert validate_date("") == False