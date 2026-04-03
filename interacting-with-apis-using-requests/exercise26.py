import requests
from typing import List, Dict, Optional, Any

def get_incident_summary(api_url: str, api_key: str, service_id: str) -> Optional[List[str]]:
    """
    Fetches open incidents for a specific service and formats them into a list
    of summary strings.

    Args:
        api_url (str): The base URL of the API.
        api_key (str): The API key for authentication.
        service_id (str): The ID of the service to query.

    Returns:
        A list of formatted incident summary strings on success, or None on an HTTP error.
    
    Raises:
        ValueError: If any argument is an empty or invalid string.
    """
    
    # 1. Validation: Ensure all arguments are non-empty strings
    args = {"api_url": api_url, "api_key": api_key, "service_id": service_id}
    for name, value in args.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")

    # 2. Prepare the request components
    endpoint = f"{api_url.rstrip('/')}/incidents"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    # Note the use of list brackets in the keys as per PagerDuty-style API spec
    params = {
        "service_ids[]": service_id,
        "statuses[]": "triggered"
    }

    try:
        # 3. Make the GET request
        response = requests.get(endpoint, headers=headers, params=params, timeout=10)
        
        # 4. Use raise_for_status to trigger HTTPError for 4xx/5xx responses
        response.raise_for_status()
        
        # 5. Parse JSON and build the list of summary strings
        data = response.json()
        incidents = data.get("incidents", [])
        
        summary_list = []
        for incident in incidents:
            # Format: "[<URGENCY>] <ID>: <Title>"
            urgency = str(incident.get("urgency", "")).upper()
            incident_id = incident.get("id", "UNKNOWN")
            title = incident.get("title", "No Title")
            
            summary_list.append(f"[{urgency}] {incident_id}: {title}")
            
        return summary_list

    except requests.exceptions.HTTPError:
        # 6. Requirement: Return None specifically on HTTP errors
        return None
    except requests.exceptions.RequestException:
        # Good practice for SRE tools: handle other network issues (timeouts, etc.)
        return None