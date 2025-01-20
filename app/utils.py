from datetime import datetime

def validate_date(date_str):
    """
        Validate a date string in the format YYYY-MM.

        Args:
            date_str (str): The date string to validate.

        Returns:
            bool: True if the date string is valid and matches the format YYYY-MM, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m")
        return True
    except ValueError:
        return False