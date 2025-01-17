import requests
from collections import Counter
from app.config import Config

def fetch_stop_and_search_data(force, date):
    """Fetch and summarize stop-and-search outcomes."""
    response = requests.get(Config.POLICE_API_URL, params={"force": force, "date": date}, timeout=10)
    response.raise_for_status()
    data = response.json()
    outcomes = Counter(item.get("outcome", "Unknown") for item in data)
    return {"total": sum(outcomes.values()), "breakdown": dict(outcomes)}

