import requests

def trigger_jenkins_job(jenkins_url: str, job_name: str, auth_token: str) -> bool:
    """
    Triggers a Jenkins job by making an authenticated POST request.

    Args:
        jenkins_url (str): The base URL of the Jenkins server.
        job_name (str): The name of the job to trigger.
        auth_token (str): The authentication token.

    Returns:
        bool: True if the job was triggered successfully (status 201), False otherwise.
    
    Raises:
        ValueError: If any argument is an empty or invalid string.
    """
    
    # 1. Validation: Ensure all arguments are non-empty strings
    args = {"jenkins_url": jenkins_url, "job_name": job_name, "auth_token": auth_token}
    for name, value in args.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")

    # 2. Construct the URL and Headers
    # Format: {jenkins_url}/job/{job_name}/build
    endpoint = f"{jenkins_url.rstrip('/')}/job/{job_name}/build"
    
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    try:
        # 3. Send the POST request
        # We don't need a 'json' or 'data' payload for a simple build trigger
        response = requests.post(endpoint, headers=headers, timeout=10)

        # 4. Return True only for 201 Created
        return response.status_code == 201

    except requests.exceptions.RequestException:
        # 5. Handle network errors (DNS, Timeout, Connection Refused)
        return False