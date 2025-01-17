from datetime import datetime

def validate_date(date_str):
    """Validate date string in YYYY-MM format."""
    try:
        datetime.strptime(date_str, "%Y-%m")
        return True
    except ValueError:
        return False