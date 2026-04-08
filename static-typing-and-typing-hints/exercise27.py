from typing import Any

# TODO: Add type hints to the function signature below.
def get_service_config(service_name: str, port: int, is_secure: bool) -> dict[str, Any]:
    """
    Creates a configuration dictionary for a service.
    """
    config = {
        "service": service_name,
        "network": {
            "port": port,
            "is_tls": is_secure
        }
    }
    return config