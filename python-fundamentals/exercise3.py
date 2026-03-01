def validate_server(server: dict) -> bool:
    """
    Validates a single server dictionary based on a set of rules.
    """
    # 1. Check if the input is a dictionary.
    if not isinstance(server, dict):
        return False

    # 2. Check for the presence of all required keys.
    required_keys = {'name', 'region', 'status'}
    if not required_keys.issubset(server.keys()):
        return False

    # 3. Check the data types and values for 'name', 'region', and 'status'.
    name = server.get('name')
    region = server.get('region')
    status = server.get('status')

    # 'name' and 'region' must be non-empty strings.
    if not (isinstance(name, str) and name.strip()):
        return False
    if not (isinstance(region, str) and region.strip()):
        return False

    # 'status' must be either 'active' or 'inactive'.
    if status not in ['active', 'inactive']:
        return False

    return True


def generate_inventory_report(servers: list[dict]) -> dict:
    """
    Processes a list of server dictionaries to generate a structured inventory report.
    """
    # 1. Handle non-list inputs gracefully.
    if not isinstance(servers, list):
        return {}

    # 2. Initialize an empty dictionary for the report.
    report = {}

    # 3. Loop through the 'servers' list.
    for server in servers:
        # 4. Call validate_server(). If it's invalid, skip it.
        if not validate_server(server):
            continue

        # 5. Extract data and build the report structure.
        region = server['region']
        status = server['status']
        name = server['name']

        # Ensure the region exists in our report dictionary
        if region not in report:
            report[region] = {
                'active': [],
                'inactive': []
            }

        # Append the server name to the appropriate status list
        report[region][status].append(name)

    # 6. Return the final report.
    return report