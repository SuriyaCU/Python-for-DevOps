import json
from pathlib import Path

def update_image_tag(config_path: str | Path, service_name: str, new_tag: str) -> None:
    """
    Reads a JSON config file, updates a service's image tag, and writes it back.
    """
    # 1. Validate config_path type and existence
    if not isinstance(config_path, (str, Path)):
        raise TypeError("config_path must be a string or a pathlib.Path object.")
    
    path_obj = Path(config_path)
    if not path_obj.exists():
        raise FileNotFoundError(f"The file {config_path} does not exist.")

    # 2. Validate service_name and new_tag
    if not isinstance(service_name, str) or not isinstance(new_tag, str):
        raise TypeError("service_name and new_tag must be strings.")
    
    if not service_name.strip() or not new_tag.strip():
        raise ValueError("service_name and new_tag cannot be empty strings.")

    # 3. Read the JSON content
    with open(path_obj, 'r') as f:
        try:
            config_data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("The provided file is not a valid JSON file.")

    # 4. Update the service tag
    # We navigate to the 'services' key as per the example structure
    services = config_data.get("services", {})
    
    if service_name not in services:
        raise KeyError(f"Service '{service_name}' not found in configuration.")
    
    services[service_name]["image_tag"] = new_tag

    # 5. Write the updated data back to the file
    with open(path_obj, 'w') as f:
        # indent=4 ensures human-readable formatting
        json.dump(config_data, f, indent=4)

# --- Quick Test ---
if __name__ == "__main__":
    # Setup dummy file
    test_file = Path("config.json")
    initial_content = {
        "deployment_name": "production-cluster",
        "services": {
            "api-gateway": {"image_tag": "1.2.0", "port": 80},
            "user-service": {"image_tag": "1.1.5", "port": 5000}
        }
    }
    
    with open(test_file, "w") as f:
        json.dump(initial_content, f)

    # Execute update
    try:
        update_image_tag(test_file, "api-gateway", "1.2.1")
        print("Update successful!")
        
        # Verify content
        with open(test_file, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if test_file.exists():
            test_file.unlink() # Cleanup