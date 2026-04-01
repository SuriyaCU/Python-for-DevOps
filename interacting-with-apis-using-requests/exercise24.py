import requests
from datetime import date

def is_today_a_public_holiday(country_code: str) -> bool:
    """
    Checks if today is a public holiday for a given country by querying an API.

    Args:
        country_code (str): The two-letter country code (e.g., "US").

    Returns:
        bool: True if today is a public holiday, False otherwise.
    
    Raises:
        TypeError: If country_code is not a string.
    """

    # Input validation
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a string")

    # (Optional but recommended strict validation)
    if len(country_code) != 2:
        raise ValueError("country_code must be a 2-letter ISO code")

    # Get today's date
    today = date.today()
    today_str = today.strftime("%Y-%m-%d")
    current_year = today.year

    # API request
    url = "https://api.example.com/v1/holidays"
    params = {
        "country": country_code,
        "year": current_year
    }

    response = requests.get(url, params=params)

    # Parse JSON response
    holidays = response.json()

    # Check if today's date is in the holiday list
    for holiday in holidays:
        if holiday.get("date") == today_str:
            return True

    return False