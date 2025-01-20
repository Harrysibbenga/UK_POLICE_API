import requests
from collections import Counter
from app.config import Config

def fetch_stop_and_search_data(force, date):
    """
        Fetches stop and search data from the police API for a given police force and date.
        
        Args:
            force (str): The identifier of the police force.
            date (str): The date for which to fetch the data in 'YYYY-MM' format.
            
        Returns:
            dict: A dictionary containing the total number of stop and search incidents and a breakdown of outcomes.
                Example:
                {
                    "total": 100,
                    "breakdown": {
                        "Arrest": 50,
                        "No further action": 30,
                        "Caution": 10,
                        "Unknown": 10
                    }
                }
                
        Raises:
            requests.exceptions.RequestException: If there is an issue with the HTTP request.
            ValueError: If the response cannot be parsed as JSON.
    """
    
    response = requests.get(Config.POLICE_API_URL, params={"force": force, "date": date}, timeout=10)
    response.raise_for_status()
    data = response.json()
    outcomes = Counter(item.get("outcome", "Unknown") for item in data)
    return {"total": sum(outcomes.values()), "breakdown": dict(outcomes)}

