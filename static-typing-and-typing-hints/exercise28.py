from typing import Optional, Any

# TODO: Add the correct type hints to this function signature.
def assign_default_role(users: list[dict[str, Any]], default_role: Optional[str] = None) -> dict[str, list[str]]:
    """
    Assigns a default role to users who have none and returns a role map.
    """
    user_roles: dict[str, list[str]] = {}
    for user in users:
        user_id = user.get("id")
        roles = user.get("roles", [])

        if not roles and default_role:
            roles.append(default_role)
        
        if user_id:
            user_roles[user_id] = roles
            
    return user_roles